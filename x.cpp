#include<iostream>
using namespace std;
class Time
{
private :
int hour, minute, second;
public :
void setTime(int h, int m, int s);
void print();

};  
void Time::setTime(int h, int m, int s)
{
hour=h;
minute=m;
second=s;
}
void Time::print()
{
cout<<"hours=\n"<<hour;
cout<<"minutes=\n"<<minute;
cout<<"seconds=\n"<<second;
}  
int main()
{
int h,m,s;
Time t1;
cout<<"Enter hours="; cin>>h;
cout<<"Enter minutes="; cin>>m;
cout<<"Enter seconds="; cin>>s;

t1.setTime(h,m,s);
t1.print();
return 0;
}
