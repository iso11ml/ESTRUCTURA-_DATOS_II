
// Isaay Sosa Hern�ndez 348713 Fecha de elaboraci�n 18-02-2023
#include <stdio.h>
#include <stdlib.h>
#define TAM 100
#define VACIO -999

typedef struct arbol{
    int value;
    char name[50];
}paciente;

paciente heap_skew[TAM];
void Inicializar();
void ShowTree();
int Insertion(int value, char name[50]);
void Intercambio(int hijo, int padre);
int Elimination();
int Max();
int Padre(int posicion);
int left(int x);
int right(int x);

int opcion, cantidad_elementos = 0;

int main(){
	int value, resultado;
	char name[50];
	Inicializar(heap_skew[100]);
	do{
		printf("\n\nMen%c principal\n", 163);
		printf("Bienvenido a Star Medica\n");
	    printf("1) Registrar paciente\n2) Conocer al siguiente paciente\n3) Atender paciente\n4) Mostrar raices \n5) Salir");
		do{
	        printf("\nIngrese la opci%cn: ", 162); scanf("%d", &opcion);
	        if(opcion < 1 || opcion > 5){
	            printf("No es una opci%cn v%clida: ", 162, 160);
	        }
	    }while(opcion < 1 || opcion > 5);

	    if(opcion ==  1){
	    	printf("\nIngrese el nivel de urgencia del nuevo paciente: "); scanf("%d", &value);
			printf("Ingrese el nombre nuevo paciente: "); scanf("%s", &name);
			resultado = Insertion(value, name);
			if(resultado == 0){
				printf("El paciente no ha puesto en lista de espera! :(\n");
			}
			else{
				printf("El paciente se encuentra en la lista de espera!\n");
			}
		}
		else if(opcion  == 2){			ShowTree();
			if(cantidad_elementos == 0){
				printf("\nNo hay pacientes en la lista de espera");
			}
			else{
				resultado = Max();
				printf("\nNivel de urgencia: %d Nombre: %s", heap_skew[resultado].value, heap_skew[resultado].name);
			}
		}
		else if (opcion == 3){
			resultado = Elimination();
			if (resultado == 0){
				printf("\nNo hay pacientes en la lista de espera!");
			}
			else{
				printf("\nEl paciente: %s ha sido atendido :)", heap_skew[0].name);
			}
		}			
		else if (opcion == 4){
			ShowTree();
		}
		
	}while(opcion != 5);
	
	return 0;
}

void Inicializar(){
	int i;
	for(i = 0; i < TAM; i++){
		heap_skew[i].value = -999;
	}
}

void ShowTree(){
	int i;
	for(i = 0; i < cantidad_elementos; i++){
		printf("Ra%cz: %d Nivel de urgencia: %d Nombre: %s\n",161, i, heap_skew[i].value, heap_skew[i].name);
	}
}

int Padre(int posicion){
	return(posicion - 1) / 2;
}
int left(int x){
	return 2 * x +1;
}

int right(int x){
	return 2 * x + 2;
}

int Insertion(int value, char name[50]){
	int hijo = cantidad_elementos;
	int padre = Padre(cantidad_elementos);

	if(heap_skew[cantidad_elementos].value == VACIO && cantidad_elementos < TAM){
		heap_skew[cantidad_elementos].value = value;
		strcpy(heap_skew[cantidad_elementos].name, name);
		if(cantidad_elementos != 0){
			while(heap_skew[hijo].value > heap_skew[padre].value){
				Intercambio(hijo, padre);
				hijo = padre;
				padre = Padre(padre);
			}
		}
		cantidad_elementos++;
		return 1;
	}
	return 0;
}

int Max(){
	return 0;
}

int Elimination(){
	if(cantidad_elementos > 0){
		Intercambio(cantidad_elementos - 1, 0);
		heap_skew[cantidad_elementos].value = VACIO;
		cantidad_elementos--;
		int padre = 0;
		int hijo;
		if(heap_skew[right(0)].value > heap_skew[left(0)].value){
			hijo = right(0);
		}
		else{
			hijo = left(0);
		}
		while(hijo < cantidad_elementos && padre <cantidad_elementos && heap_skew[hijo].value > heap_skew[padre].value){
			Intercambio(hijo, padre);
			padre = hijo;
			if(heap_skew[left(padre)].value < heap_skew[right(padre)].value){
				hijo = left(padre);
			}
			else{
				hijo = right(padre);
			}
		}
		return 1;
	}
	return 0;
}

void Intercambio(int hijo, int padre){
	int valor_auxiliar = heap_skew[hijo].value;
	char nombre_auxiliar[50];
	strcpy (nombre_auxiliar, heap_skew[hijo].name );
	heap_skew[hijo].value = heap_skew[padre].value;
	strcpy (heap_skew[hijo].name,heap_skew[padre].name );
	heap_skew[padre].value = valor_auxiliar;
	strcpy (heap_skew[padre].name,nombre_auxiliar );
}
