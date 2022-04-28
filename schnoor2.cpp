#include <bits/stdc++.h>
using namespace std;
#define ld long long

ld ModInv(ld b, ld n){
  ld r1=n,r2=b,t1=0,t2=1;
  while(r2>0){
    ld q=r1/r2;
    ld r=r1-q*r2;
    r1=r2;r2=r;
    ld t=t1-q*t2;
    t1=t2;t2=t;
  }
  if(t1<0)t1+=n;
  return t1;
}

ld powerLL(ld x, ld n, ld MOD) { 
	ld result = 1; 
	while (n) { 
		if (n&1) 
			result = result * x % MOD; 
		n = n / 2; 
		x = x * x % MOD; 
	} 
	return result; 
} 

ld powerStrings(string sa, string sb, ld MOD) { 

	ld a = 0, b = 0; 
	for (int i = 0; i < sa.length(); i++) 
		a = (a * 10 + (sa[i] - '0')) % MOD; 

	for (int i = 0; i < sb.length(); i++) 
		b = (b * 10 + (sb[i] - '0')) % (MOD - 1); 
	return powerLL(a, b, MOD); 
} 

ld mod(string num, ld a) { 
	ld res = 0; 

	// One by one process all digits of 'num' 
	for (int i = 0; i < num.length(); i++) 
		res = (res*10 + (int)num[i] - '0') %a; 

	return res; 
} 


int main(){
  ld p,q,e0,d,m,r,MOD;
  cin>>p>>q>>e0>>d>>m>>r;
  //2267 103 2 30 1000 11
  ld a,b,t,bef_v,bef_s1,e1,e2,s1,s2,v;
  e1=powerStrings(to_string(e0),to_string((p-1)/q),p);
  if(e1<0)e1+=p;
  e2=powerStrings(to_string(e1),to_string(d),p);
  if(e2<0)e2+=p;
  
  ////////// For concate  S1 we are finding both components
  a=powerStrings(to_string(e1),to_string(r),p);
  if(a<0)a+=p;
  bef_s1=stoll(to_string(m)+to_string(a),NULL,10);

  s1=200;
  
  s2=(r+((d*s1)%q))%q;
  
  //////////////// fro concate V we are finding both components
  a=powerStrings(to_string(e1),to_string(s1),p);
  if(a<0)a+=p;
  b=powerStrings(to_string(e2),to_string(s2),p);
  if(b<0)b+=p;
  t=(a*b)%p;
  
  bef_v=stoll(to_string(m)+to_string(t),NULL,10);
  
  cout<<"e1="<<e1<<"\n";
  cout<<"e2="<<e2<<"\n";
  cout<<"s2="<<s2<<"\n";
  cout<<"bef_s1="<<bef_s1<<"\n";
  cout<<"bef_v="<<bef_v<<"\n";
    
}
