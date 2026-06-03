#include<iostream>
using namespace std;
// class A{
//     public:
//     void showA(){
//         cout<<"Hello A"<<endl;
//     }
// };

// class B:public A{
//     public:
//     void show(){
//         cout<<"Hello B"<<endl;
//     }
// };

// class C:public A{
//     public:
//     void show(){
//         cout<<"Hello C"<<endl;
//     }
// };

// class D: public B, public C {
//     public:
//     void show(){
//         cout<<"Hello D"<<endl;
//     }
// };

class A{
    public:
    virtual void area()=0;
};
class B:public A{
    public:
    void area(){
        cout<<"Hello";
    }
};

int main(){
  A obj ;
  obj.area();
}