#include<iostream>
using namespace std;
int x[2][100][200];

int solve(string s,int i,int j,bool isTrue){
	int t=0;
	if(isTrue==true){
		t=1;
	}else{
		t=0;
	}
	if(x[t][i][j]>-1){
		return x[t][i][j];
	}
	if(i>j){
		return 0;
	}
	if(i==j){
		if(isTrue){
			return s[i]=='T';
		}
		else{
			return s[i]=='F';
		}
	}
	int ans=0;
	for(int k=i+1;k<j;k=k+2){
		x[1][i][k-1]=solve(s,i,k-1,true);
		int LT=x[1][i][k-1];
		x[0][i][k-1]=solve(s,i,k-1,false);
        int LF=x[0][i][k-1];
        x[1][k+1][j]=solve(s,k+1,j,true);
        int RT=x[1][k+1][j];
        x[0][k+1][j]=solve(s,k+1,j,false);
        int RF=x[0][k+1][j];
		
		if(s[k]=='&'){
			if(isTrue){
				ans=ans+(LT*RT);
			}
			else{
				ans=ans+(LF*RT+LT*RF+LF*RF);
			}
		}
		if(s[k]=='|'){
			if(isTrue){
            ans=ans+(LT*RT+LF*RT+LT*RF);
			}
			else{
				ans=ans+(LF*RF);
			}
		}
		if(s[k]=='^'){
			if(isTrue){
                ans=ans+(LF*RT+LT*RF);
			}
			else{
                ans=ans+(LT*RT+LF*RF);
			}
		}
	}
	return ans;
}


int main(){
	string s="T^F&T";
	int i=0;
	int j=s.size()-1;
	for(int k=0;k<2;k++){
	for(int i=0;i<100;i++){
		for(int j=0;j<200;j++){
		x[k][i][j]=-1;
		}
	}
}
	int ways=solve(s,i,j,true);
	cout<<ways;
	return 0;
}
