  #include <bits/stdc++.h>  
using namespace std;
 

typedef long long int ll;
typedef vector<int> vi;
typedef vector<char> vc;
typedef pair<int, int> pi;
typedef pair<ll, ll> pll;
 
const int mod = 1e9 + 7;
const int INF = 1LL << 29;
 

#define mp make_pair
#define el putchar('\n')
#define sp putchar(' ')
#define all(a) a.begin(),a.end()
 
#define getx getchar_unlocked
#define putx putchar_unlocked
#define in(n) scanf("%d",&n)
#define inl(n) scanf("%lld",&n)
#define out(n) printf("%d",n);
#define outl(n) printf("%lld",n);
 
inline int getint(){ 
    char _c;
    int _x=0;
    _c=getx();
    while (_c<=' ') _c=getx();
    while (_c>='0'){ _x=10*_x+(_c-'0'); _c=getx();}
    return _x;
}
 
inline void outint(int _x){
    char _str[16];
    int _i=0;
    if (_x==0) putx('0');
    else{
    while (_x>0){ _str[_i++]=(_x%10)+'0'; _x=_x/10; }
    while (_i) putx(_str[--_i]); }
    putx('\n');
}
 
void m2_2(int r,int c)
{
    printf("%d %d %d %d \n",r+1,c+1,r+2,c+1);
    printf("%d %d %d %d \n",r+1,c+2,r+2,c+2);
    printf("%d %d %d %d \n",r+1,c+1,r+1,c+2);
    printf("%d %d %d %d \n",r+2,c+1,r+2,c+2);
}
 
void m4_4(int r,int c)
{
        m2_2(r,c);
        m2_2(r,c+2);
        m2_2(r+2,c);
        m2_2(r+2,c+2);
        
        m2_2(r+1,c+1);
        
        m2_2(r,c);
        m2_2(r,c+2);
        m2_2(r+2,c);
        m2_2(r+2,c+2);
    
}
 
void m8_8(int r,int c)
{
        m4_4(r,c);
        m4_4(r,c+4);
        m4_4(r+4,c);
        m4_4(r+4,c+4);
        
        m4_4(r+2,c+2);
        
        m4_4(r,c);
        m4_4(r,c+4);
        m4_4(r+4,c);
        m4_4(r+4,c+4);
    
}
 
void m1_2(int r,int c) 
{
    printf("%d %d %d %d \n",r+1,c+1,r+1,c+2);
}
 
void m2_1(int r,int c) 
{
    printf("%d %d %d %d \n",r+1,c+1,r+2,c+1);
}
 
void m1_4(int r,int c) 
{
    printf("%d %d %d %d \n",r+1,c+1,r+1,c+2);
    printf("%d %d %d %d \n",r+1,c+3,r+1,c+4);
    printf("%d %d %d %d \n",r+1,c+2,r+1,c+3);
    printf("%d %d %d %d \n",r+1,c+3,r+1,c+4);
    printf("%d %d %d %d \n",r+1,c+2,r+1,c+3);
    printf("%d %d %d %d \n",r+1,c+1,r+1,c+2);
    printf("%d %d %d %d \n",r+1,c+3,r+1,c+4);
}
 
void m1_5(int r,int c) 
{
    m1_4(r,c+1);
    printf("%d %d %d %d \n",r+1,c+1,r+1,c+2);
    m1_4(r,c+1);
}
 
void m4_1(int r,int c) 
{
    printf("%d %d %d %d \n",r+1,c+1,r+2,c+1);
    printf("%d %d %d %d \n",r+3,c+1,r+4,c+1);
    printf("%d %d %d %d \n",r+2,c+1,r+3,c+1);
    printf("%d %d %d %d \n",r+3,c+1,r+4,c+1);
    printf("%d %d %d %d \n",r+2,c+1,r+3,c+1);
    printf("%d %d %d %d \n",r+1,c+1,r+2,c+1);
    printf("%d %d %d %d \n",r+3,c+1,r+4,c+1);
}
 
void m5_1(int r,int c) 
{
    m4_1(r+1,c);
    printf("%d %d %d %d \n",r+1,c+1,r+2,c+1);
    m4_1(r+1,c);
}
 
void m1_7(int r,int c) 
{
    m1_4(r,c+3);
    m1_4(r,c);
    m1_4(r,c+3);
}
 
void m7_1(int r,int c) 
{
    m4_1(r+3,c);
    m4_1(r,c);
    m4_1(r+3,c);
}
 
void m1_11(int r,int c)
{
    m1_4(r,c);
    m1_7(r,c+4); 
    m1_2(r,c+3);
    
    m1_4(r,c);
    m1_7(r,c+4);
}
 
void m11_1(int r,int c) 
{
    m4_1(r,c);
    m7_1(r+4,c);
    m2_1(r+3,c);
    
    m4_1(r,c);
    m7_1(r+4,c);
}
 
void m1_8(int r,int c) 
{
    m1_4(r,c+4);
    m1_5(r,c);
    m1_4(r,c+4);
}
 
void m8_1(int r,int c) 
{
    m4_1(r+4,c);
    m5_1(r,c);
    m4_1(r+4,c);
}
 
 
void m1_13(int r,int c)
{
    m1_5(r,c);
    m1_8(r,c+5);
    m1_4(r,c+3);
    
    m1_4(r,c);
    
    m1_4(r,c+6);
    m1_4(r,c+9);
    
}
 
void m13_1(int r,int c)
{
    m5_1(r,c);
    m8_1(r+5,c);
    m4_1(r+3,c);
    
    m4_1(r,c);
    
    m4_1(r+6,c);
    m4_1(r+9,c);
    
}
 
void m1_20(int r,int c)
{
    m1_7(r,c);
    m1_13(r,c+7);//72
    m1_2(r,c+6);
    
    m1_4(r,c+3);
    m1_4(r,c);
    
    m1_4(r,c+7);
    m1_4(r,c+10);
    m1_4(r,c+13);
    m1_4(r,c+16);
}
 
void m20_1(int r,int c)
{
    m7_1(r,c);
    m13_1(r+7,c);
    m2_1(r+6,c);
    
    m4_1(r+3,c);
    m4_1(r,c);
    
    m4_1(r+7,c);
    m4_1(r+10,c);
    m4_1(r+13,c);
    m4_1(r+16,c);
}
 
int main () 
{
    
    int n,r,c;
    n=getint();
    if(n==2)
    {
        printf("4\n");
        m2_2(0,0);
    }
    else if(n==4)
    {
        printf("36\n");
/*        
        m2_2(0,0);
        m2_2(0,2);
        m2_2(2,0);
        m2_2(2,2);
        
        m2_2(1,1);
        
        m2_2(0,0);
        m2_2(0,2);
        m2_2(2,0);
        m2_2(2,2);
*/
m4_4(0,0);
    }
    else if(n==5)
    {
        printf("150\n");
        
        for(r=0;r<5;++r)
        {
            m1_5(r,0);
        }
        for(c=0;c<5;++c)
        {
            m5_1(0,c);
        }
           
    }
    else if(n==8)
    {
        printf("324\n");
/*        
        m4_4(0,0);
        m4_4(0,4);
        m4_4(4,0);
        m4_4(4,4);
        
        m4_4(2,2);
        
        m4_4(0,0);
        m4_4(0,4);
        m4_4(4,0);
        m4_4(4,4);
        */
        
m8_8(0,0);        
    }
    else if(n==11)
    {
        printf("1254\n");
        
        for(r=0;r<11;++r) 
        {
            m1_11(r,0);
        }
        for(c=0;c<11;++c) 
        {
            m11_1(0,c);
        }
           
    }
    else if(n==13)
    {
        printf("1872\n");
        
        for(r=0;r<13;++r) 
        {
            m1_13(r,0);
        }
        for(c=0;c<13;++c) 
        {
            m13_1(0,c);
        }
        
    }
    else if(n==16)
    {
        printf("2916\n");
        
        m8_8(0,0);
        m8_8(0,8);
        m8_8(8,0);
        m8_8(8,8);
        
        m8_8(4,4);
        
        m8_8(0,0);
        m8_8(0,8);
        m8_8(8,0);
        m8_8(8,8);
        
    }
    else if(n==20)
    {
        printf("5440\n");
        
        for(r=0;r<20;++r) 
        {
            m1_20(r,0);
        }
        for(c=0;c<20;++c) 
        {
            m20_1(0,c);
        }
        
    }
    
    return 0;
}
