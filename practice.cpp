#include<iostream>
using namespace std;
int main(){
cout<<"This is my first programm!"<<endl;
double num1;
cout<<"Enter a Number:";
cin>>num1;
char op;
cout<<"Enter a opreator(+,-,*,/,%):";
cin>>op;
double num2;
cout<<"Enter a Number:";
cin>>num2; 
if(op=='+'){
    cout<<"Sum:"<<num1+num2<<endl;
}
else if (op=='-')
{cout<<"Sub:"<<num1-num2<<endl;
}
else if(op=='*'){
    cout<<"Multi:"<<num1*num2<<endl;
} 
else if(op=='/'){
    if(num2!=0){
        cout<<"Dev:"<<num1/num2<<endl;
        
    }
    else{
        cout<<"Undefined Error!"<<endl;
    }}

else{
    cout<<"Invalid Opreator! please!check"<<endl;
}

}






