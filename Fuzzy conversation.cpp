#include <iostream>
using namespace std;
typedef long long int ll;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
    	ll a,b,c,x,y,z;
    	int sum = 0;
    	cin>>a>>b>>c>>x>>y>>z;
    	int p=0,q=0;
    	if(a+b+c == 0){
    	    p = 1;
    	}
    	if(x+y+z==0){
    	    q = 1;
    	}
    	if(p == 1 && q == 1){
    	    cout<<sum<<endl;
    	}
    	else if(p+q == 1){
    	    if((a+x)%2==1) sum++;
    	    if((b+y)%2==1) sum++;
    	    if((c+z)%2==1) sum++;
    	    if(sum == 0 || sum == 3) cout<<2<<endl;
    	    else cout<<1<<endl;
    	}
    	else{
    	     if(abs(a-x)%2==1) sum++;
    	    if(abs(b-y)%2==1) sum++;
    	    if(abs(c-z)%2==1) sum++;
    	     if(sum == 1||sum ==2) cout<<1<<endl;
    	     else cout<<0<<endl;
    	}
    	
	}
	return 0;
}

