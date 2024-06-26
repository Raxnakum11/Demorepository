#include <iostream>
using namespace std;



bool can_pairs(int arr[],int num,int k){
    //check odd
  if(num%2==1)return false;
 int count=0;
 int visited[num];

for(int k=0;k<num;k++){
    visited[k]=-1;
}

 for(int i=0;i<=num;i++){
    for(int j=i+1;j<num;j++){

            if((arr[i]+arr[j])%k==0 &&visited[i]==-1&&visited[j]==-1){
                    count++;
               visited[i]=1;
               visited[j]=1;
               cout<<"("<<i<<","<<j<<")"<<endl;

            }
 }

}

  if(count==num/2){
  return true;
  }
  else {return false;}
}
 int main(){
 int arr[6]={3,1,2,6,9,4},k=5;

int num=sizeof(arr)/sizeof(arr[0]);
can_pairs(arr,num,k)?cout<<"True":cout<<"False";
return 0;
 }
