#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ALPHABET_SIZE 26

// Estructura del nodo del trie
struct TrieNode {
    struct TrieNode* children[ALPHABET_SIZE];
    int isEndOfWord;
};

// Función para crear un nuevo nodo del trie
struct TrieNode* createNode() {
    struct TrieNode* node = (struct TrieNode*)malloc(sizeof(struct TrieNode));
    node->isEndOfWord = 0;
    for (int i = 0; i < ALPHABET_SIZE; i++) {
        node->children[i] = NULL;
    }
    return node;
}

// Función para insertar una palabra en el trie
void Inserta_palabra(struct TrieNode* root, char* word) {
    int length = strlen(word);
    struct TrieNode* current = root;
    for (int i = 0; i < length; i++) {
        int index = word[i] - 'a';
        if (current->children[index] == NULL) {
            current->children[index] = createNode();
        }
        current = current->children[index];
    }
    current->isEndOfWord = 1;
}

// Función para buscar una palabra en el trie
int Buscar_palabra(struct TrieNode* root, char* word) {
    int length = strlen(word);
    struct TrieNode* current = root;
    for (int i = 0; i < length; i++) {
        int index = word[i] - 'a';
        if (current->children[index] == NULL) {
            return 0;
        }
        current = current->children[index];
    }
    return (current != NULL && current->isEndOfWord);
}

int main() {
    struct TrieNode* root = createNode();
    Inserta_palabra(root, "hola");
    Inserta_palabra(root, "que");
    Inserta_palabra(root, "programming");
    Inserta_palabra(root, "is");
    Inserta_palabra(root, "fun");
}