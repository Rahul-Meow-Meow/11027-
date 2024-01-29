#include<stdio.h>
int func(int n){
	return 17+9*n;
}
void main(){
int sum = 0;
for (int i = 0; func(i)<=350; i++){
	sum += func(i);
}
printf("%d\n",sum);
}
