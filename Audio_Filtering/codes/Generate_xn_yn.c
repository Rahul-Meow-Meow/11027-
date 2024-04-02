#include <stdio.h>
#include <math.h>
int x(int n){
	int output;
	if(0<=n && n<=3){
		output = n+1;
	}
	else if (3<n && n<=5){
		output = 6-n;
	}
	else{
		output = 0;
	}
	return output;
}
void main(){
	FILE *fptr = fopen("Generated_values_xn_yn.txt", "w");
	double y[20];
	y[0] = x(0);
	fprintf(fptr, "1 %d %f \n",x(0),y[0]);
	for(int i = 1; i < 20; i++){
		y[i] = -0.5*y[i-1]+x(i)+x(i-2);
		fprintf(fptr, "%d %d %f \n",(i+1),x(i),y[i]);
	}
	fclose(fptr);
//printf("%d",x(7));
}
