#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(void){
	FILE *fe=NULL,*fs=NULL;
	uint8_t sample;
	int nbR, indent=0;
	fe=fopen("./data", "r");
	if(!fe){
		perror("Error : can't open ./data");
		return -1;
	}
	fs=fopen("./data.txt","w");
	if(!fs){
		perror("Error : can't open ./data.txt");
		fclose(fe);
		return -2;
	}
	while((nbR=fread(&sample, sizeof(uint8_t), 1, fe))>0){
		fprintf(fs, "%0.2x",sample);
		indent+=2;
		if(indent%80==0){
			fprintf(fs, "\n");
			indent=0;
		}
	}
	fclose(fe);
	fclose(fs);
	return 0;
}
