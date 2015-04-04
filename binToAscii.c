#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

/*Rappelons que le calcul bit par bit du syndrome doit être exécuté
 *  en moins de 842µs (durée d'1 bit RDS)*/
 
enum groupType{
	TYPE_0A  =  0 + 0,
	TYPE_0B  =  0 + 1,
	TYPE_1A  =  2 + 0,
	TYPE_1B  =  2 + 1,
	TYPE_2A  =  4 + 0,
	TYPE_2B  =  4 + 1,
	TYPE_3A  =  6 + 0,
	TYPE_3B  =  6 + 1,
	TYPE_4A  =  8 + 0,
	TYPE_4B  =  8 + 1,
	TYPE_5A  = 10 + 0,
	TYPE_5B  = 10 + 1,
	TYPE_6A  = 12 + 0,
	TYPE_6B  = 12 + 1,
	TYPE_7A  = 14 + 0,
	TYPE_7B  = 14 + 1,
	TYPE_8A  = 16 + 0,
	TYPE_8B  = 16 + 1,
	TYPE_9A  = 18 + 0,
	TYPE_9B  = 18 + 1,
	TYPE_10A = 20 + 0,
	TYPE_10B = 20 + 1,
	TYPE_11A = 22 + 0,
	TYPE_11B = 22 + 1,
	TYPE_12A = 24 + 0,
	TYPE_12B = 24 + 1,
	TYPE_13A = 26 + 0,
	TYPE_13B = 26 + 1,
	TYPE_14A = 28 + 0,
	TYPE_14B = 28 + 1,
	TYPE_15A = 30 + 0,
	TYPE_15B = 30 + 1
};


int main(void){
	FILE *fe=NULL,*fs=NULL;
	float sample;
	uint8_t low,high;
	uint8_t tab[16]={0,0,0,0,0,0,0,1,0,1,1,1,1,1,1,1};
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
	printf("Float=%d\n",sizeof(float));
	while((nbR=fread(&sample, sizeof(float), 1, fe))>0){
		/*
		high=sample>>4;
		low=sample<<4;
		low>>=4;
		fprintf(fs,"%d%d",tab[high],tab[low]);*/
		fprintf(fs,"%f\n",sample);
		indent+=1;
		if(indent%4==0){
			fprintf(fs, "\n");
			indent=0;
		}
	}
	fclose(fe);
	fclose(fs);
	return 0;
}
