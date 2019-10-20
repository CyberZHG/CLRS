/******************************************
*    AUTHOR:         Atharva Sarage       *
*    INSTITUITION:   IIT HYDERABAD        *
******************************************/
#include<bits/stdc++.h>
#warning Check Max_Limit,Overflows
using namespace std;
# define IOS ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
# define ff first
# define ss second
# define pb push_back
# define mod 1000000007
# define ll long long 
# define db double
# define inf 1e9
# define mx2 100005
# define mx 1000005
int a[mx];
int curr=1;
vector <pair<pair<int,int>,int>> vec;
int solve(int l,int r,int x)
{
	//cout<<l<<" "<<r<<" "<<x<<"\n";
	if(l==r)
		return (a[l]-x==1);

	int max1=0,max2=0,min1=inf,min2=inf;

	for(int i=0;i<=(l+r)/2-l;i++)
	{	
		//printf("???\n");
		max1=max(max1,a[l+i]);
		min1=min(min1,a[l+i]);
		max2=max(max2,a[r-i]);
		min2=min(min2,a[r-i]);
		//cout<<max1<<" "<<max2<<"\n";
		if(max1==i+1+x)
		{
			//printf("*\n");
			int w1=solve(l,l+i,x);
			int w2=solve(l+i+1,r,i+1+x);
			if(!w1 || !w2)
				return 0;
			vec.pb({{w1,w2},1});
			return ++curr;
		}
		else if((max1-min1+1)==i+1 && max1==(r-l+1+x))
		{
			int w1=solve(l,l+i,(r-l)-i+x);
			int w2=solve(l+i+1,r,x);
			//printf("**\n");
			if(!w1 || !w2)
				return 0;
			vec.pb({{w1,w2},2});
			return ++curr;
		}
		else if((max2-min2+1)==i+1 && max2==(r-l+1+x))
		{
			//printf("***\n");
			int w1=solve(l,r-i-1,x);
			int w2=solve(r-i,r,x+(r-l)-i);
			if(!w1 || !w2)
				return 0;
			vec.pb({{w1,w2},1});
			return ++curr;
		}
		else if(max2==i+1+x)
		{
			//printf("****\n");
			int w1=solve(l,r-i-1,i+1+x);
			int w2=solve(r-i,r,x);
			vec.pb({{w1,w2},2});
			if(!w1 || !w2)
				return 0;
			return ++curr;
		}
	}	
	return 0;
}
int main()
{
	IOS;
	int t;
	cin>>t;
	while(t--)	
	{
		int n;
		cin>>n;
		for(int i=1;i<=n;i++)
			{
				cin>>a[i];
				//cout<<a[i]<<" ";
			}
		//cout<<"\n";
		if(solve(1,n,0))
		{
			cout<<"YES"<<"\n";
			cout<<vec.size()<<endl;
			for(auto k:vec)
				cout<<k.ff.ff<<" "<<k.ff.ss<<" "<<k.ss<<"\n";
		}
		else
		{
			// for(int i=1;i<=n;i++)
			// 	cout<<a[i]<<" ";
			// cout<<"\n";
			cout<<"NO"<<"\n";
		}

		vec.clear();
		curr=1;
	}
}

