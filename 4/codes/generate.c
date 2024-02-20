#include<stdio.h>
#include<stdlib.h>
int u(float t,int t_0){
	if(t>=t_0){
		return 1;
	}
	else{
		return 0;
	}
}
/*void append(*ptr, len, add){
	ptr = (int *)realloc(ptr, sizeof(int)*(len+1));
	*(ptr+len) = add;*/

void main(){
	FILE *fptr;
	fptr = fopen("Values.txt","w");
	//int *ptr = (int*)malloc(int(s))
	float t = -3;
	for(int i = 0; i <=1000 ; i++){
		t = t+ (1/100.0);
		//printf("%f ,", t);
		float value = t*u(t,0) + (t-2)*u(t,2) -2*(t-1)*u(t,1);
		fprintf(fptr, "%.3f %.3f\n", t, value);
	}
}
