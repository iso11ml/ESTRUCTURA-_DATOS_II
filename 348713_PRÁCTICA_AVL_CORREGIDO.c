#include <stdio.h>
#include <stdlib.h>


typedef struct structure_node
{
    int key;
    struct structure_node *left, *right, *dad;
}nodo;

nodo *root = NULL;
nodo *posicion_anterior = NULL;


nodo *Search(int value);
nodo *Insertion(int value);
nodo *Max(nodo *pointer);
nodo *Min(nodo *pointer);
int Eliminate(int value);
int Altura(nodo *pointer);
int FactorEquilibrio(nodo *pointer);
void Balanceo(nodo *pointer);
void LeftRotation(nodo *pointer);
void RightRotation(nodo *pointer);
void DoubleLeftRotation(nodo *pointer);
void DoubleRightRotation(nodo *pointer);


int main() {
    int opcion, valor;
    nodo *pointer;
    do {
        printf("\n1) Insertar\n2) Eliminar\n3) Buscar\n4) M%cximo \n5) M%cnimo\n6) Salir", 160, 161 );
        printf("\nOpcion: "); scanf("%i",&opcion);
        switch(opcion){
            case 1:
				printf("\nInserte el valor: "); 
				scanf("%d",&valor);
                pointer = Insertion(valor);
                if(pointer == NULL){
                    printf("\nEl valor no se pudo insertar!");
                }
                else{
                    printf("\nEl valor se ha insertado exitosamente!");
                }
                break;
            case 2: 
                printf("\nIngrese el valor que desea eliminar: "); scanf("%d",&valor);
                int resultado = Eliminate(valor);
                if (resultado == 0){
                    printf("El valor no se pudo eliminar debido a que no existe o no hay datos en el %crbol!", 160);
                }
                else{
                    printf("El valor se ha elimiando correctamente");
                }
                break;
            case 3: 
				printf("\nValor a buscar: "); scanf("%d",&valor);
                pointer = Search(valor);
                if(pointer == NULL){
                    printf("\nNo esta en el %crbol", 160);
                }
                else{
                    printf("\nSi esta en el %crbol", 160);
                    int factor_nodo = FactorEquilibrio(pointer); 
    				///printf("\nEl factor de equilibrio del nodo es: %d", factor_nodo);
                }
                break;
            case 4: 
				pointer = Max(root);
                if(pointer != NULL){
                    printf("\nEl m%cximo es %i",160,  pointer -> key);
                }
    
                else{
                    printf("\nEl %crbol esta vac%co, no hay m%cximo", 160, 161, 160);
                }
                break;
            case 5: pointer = Min(root);
            if(pointer != NULL)
                printf("\nEl m%cnimo es %i",161, pointer -> key);
            else
                printf("\nEl %crbol esta vac%co, no hay m%cnimo", 160, 161, 161);
            break;

        }
    } while (opcion != 6);
    return 0;
}

nodo *Search(int value){
    nodo *nodo_auxiliar;
    nodo_auxiliar = root;
   
    while(nodo_auxiliar != NULL && nodo_auxiliar -> key != value){
        posicion_anterior = nodo_auxiliar;
        if(value < nodo_auxiliar -> key){
            nodo_auxiliar = nodo_auxiliar -> left;
        }
        else{
            nodo_auxiliar = nodo_auxiliar -> right;
        }  
    }
    return nodo_auxiliar;
}

nodo *Insertion(int value){
    nodo *pointer = NULL;
    pointer = Search(value);
    if(pointer == NULL){
        pointer = (nodo *)malloc(sizeof(nodo));
        if(pointer != NULL){
            pointer -> key = value;
            pointer -> dad = posicion_anterior;
            pointer -> left = pointer -> right = NULL;
        }
        if(root == NULL){
            root = pointer;
        }
        else if(value < posicion_anterior -> key){
        	posicion_anterior -> left = pointer;
		}
        else{
        	posicion_anterior -> right = pointer;
		}
		
		Balanceo(posicion_anterior);
		return pointer;
    }
    return pointer;
}

nodo *Max (nodo *pointer){
    nodo *nodo_auxiliar;
    nodo_auxiliar = pointer;
    if(nodo_auxiliar != NULL)
        while(nodo_auxiliar -> right != NULL)
            nodo_auxiliar = nodo_auxiliar -> right;
    return nodo_auxiliar;
}

nodo *Min (nodo *pointer){
    nodo *nodo_auxiliar;
    nodo_auxiliar = pointer;
    if(nodo_auxiliar != NULL)
        while(nodo_auxiliar -> left != NULL)
            nodo_auxiliar = nodo_auxiliar -> left;
    return nodo_auxiliar;
}


int Altura(nodo *pointer){
    int contador_derecho = 0, contador_izquierdo = 0;
    nodo *nodo_auxiliar;
    nodo_auxiliar = pointer;
    if (nodo_auxiliar != NULL){
    	int altura_izquierda = Altura(nodo_auxiliar -> left);
    	int altura_derecha = Altura(nodo_auxiliar -> right);
    	if(altura_izquierda > altura_derecha){
    		return altura_izquierda + 1;
		}
        else{
			return altura_derecha + 1;
		}
	}
    else{
		return 0;
	}
}

int FactorEquilibrio(nodo *pointer){
	return Altura(pointer -> right) - Altura(pointer -> left);
}

int Eliminate(int value){
    int bandera = 0; // False
    nodo *posicion_actual = Search(value);
    nodo *nodo_auxiliar;
    nodo *padre;
    nodo *nieto;
    nodo *abuelo;
    if (posicion_actual != NULL) {
        //Caso 1: Soy hoja y no tengo hijos
        if (posicion_actual -> left == NULL && posicion_actual -> right == NULL){
                nodo_auxiliar = posicion_actual -> dad;
                if (posicion_actual -> dad == NULL){
                    posicion_actual -> key = NULL;
                }
                //Avisarle al nodo pare que ya no tiene hijo
                else if(nodo_auxiliar -> right == posicion_actual){ 
                    nodo_auxiliar -> right = NULL;
                }
                else{
                    nodo_auxiliar -> left = NULL;
                }
            posicion_actual -> key = NULL;
            return bandera = 1;
        }
        // Caso 2: Tengo uno de mis dos hijos
        if (posicion_actual -> left == NULL || posicion_actual -> right == NULL){
            
            abuelo = posicion_actual -> dad; 
            if(posicion_actual -> right == NULL){
                nieto = posicion_actual -> left;
            }
            else{
                nieto = posicion_actual -> right;
            }
            if(abuelo -> right == posicion_actual){
                abuelo -> right = nieto;
            }
            else{
                abuelo -> left = nieto;
            }
            return 1;
        }
        // Caso 3: Tengo 2 hijos
        else{
            if (posicion_actual -> key < root -> key){ 
                padre = Max(root -> left);
            
            }else{
                padre = Min(root -> right);
            }

            if(padre -> right == posicion_actual){
               padre -> right = NULL; 
            }
            else{
                padre -> left = NULL;
            }
            posicion_actual -> key = padre -> key;
            padre -> key = NULL;
            return 1;
        }
    }
    return 0;  
}

void Balanceo(nodo *pointer){
	nodo *auxiliar;
	if(pointer != NULL){
		auxiliar = pointer -> dad;
		int factor = FactorEquilibrio(pointer);
		if(factor > 1){ 
			if(FactorEquilibrio(pointer -> right) < 0){
				DoubleLeftRotation(pointer);
			}else{
				LeftRotation(pointer);
			}			
		}else if(factor < -1){ 
			if(FactorEquilibrio(pointer -> left) > 0){
				DoubleRightRotation(pointer);
			}else{
				RightRotation(pointer);
			}
		}
		//Balanceo(auxiliar);
	}
}

void LeftRotation(nodo *pointer){
    nodo *pointer_p;
    nodo *pointer_q;
    nodo *auxiliar;
    auxiliar = pointer -> right;
    pointer_q = auxiliar -> left;
    pointer_p = pointer -> dad;
    pointer -> right = pointer_q;
    auxiliar -> left = pointer;

    if(pointer_q != NULL){
        pointer_q -> dad = pointer;
    }
    pointer -> dad = auxiliar;
    if(pointer_p == NULL){
        root -> dad = auxiliar ;
    }
    else{
        auxiliar -> dad = pointer_p;
        if(auxiliar -> key > pointer_p -> key){
            pointer_p -> right = auxiliar;
        }
        else{
            pointer_p -> left = auxiliar;
        }
    }
}

void RightRotation(nodo *pointer){
    nodo *pointer_p;
    nodo *pointer_q;
    nodo *auxiliar;
    auxiliar = pointer -> left;
    pointer_q = auxiliar -> right;
    pointer_p = pointer -> dad;
    pointer -> left = pointer_q;
   auxiliar -> right = pointer;

    if(pointer_q != NULL){
        pointer_q -> dad = pointer;
    }
    pointer -> dad = auxiliar;
    if(pointer_p == NULL){
        root = auxiliar ;
    }
    else{
        auxiliar -> dad = pointer_p;
        if(auxiliar -> key > pointer_p -> key){
            pointer_p -> right = auxiliar;
        }
        else{
            pointer_p -> left = auxiliar;
        }
    }
}

void DoubleLeftRotation(nodo *pointer){
    nodo * auxiliar;
    auxiliar = pointer -> right;
    RightRotation(pointer -> right);
    LeftRotation(pointer);
}

void DoubleRightRotation(nodo *pointer){
    LeftRotation(pointer -> left);
    RightRotation(pointer);
}

