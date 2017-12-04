#include "lists.h"

/**
 * check_cycle - Checks if there is a loop in a linked list.
 * @list: A pointer to the head of the linked list.
 * Return: 0 if there is not a loop, 1 if there is a loop.
 */
int check_cycle(listint_t *list)
{
	int size;
	int value;
	size_t *array;
	size_t *address_array;

	if (list == NULL)
		return (0);
	/*Allocating space for initial value*/
	address_array = malloc(sizeof(size_t) * 1);
	if (address_array == NULL)
		return (0);
	address_array[0] = (size_t)list;
	for (size = 1; list != NULL; size++)
	{
		/*Adding space to the array*/
		array = add_to_array(&address_array, size + 1);
		if (array == 0)
			return (0);
		/*Checking if an address exist on the array*/
		value = check_address(array, list->next, size - 1);
		if (value == 1)
		{
			free(array);
			return (1);
		}
		/*Adding address to the array*/
		array[size - 1] = (size_t)list;
		list = list->next;
	}
	free(array);
	return (0);
}

/**
 * add_to_array - Adds space to an array.
 * @address_array: A pointer to an array of size_t values.
 * @size: The new size necesary to store the array.
 * Return: If sucessful the address of the new allocated array. Otherwise 0.
 */
size_t *add_to_array(size_t **address_array, int size)
{
	if (address_array == NULL)
		return (0);
	*address_array = realloc(*address_array, size * sizeof(size_t));
	if (*address_array == NULL)
		return (0);
	return (*address_array);
}

/**
 * check_address - Checks if an address is already stored in the array.
 * @array: Pointer to an array of values representing the address of each node
 * in a linked list.
 * @list: Pointer to an element of the list.
 * @size: The size of the array containing the address.
 * Return: 1 if address is in the array, 0 otherwise.
 */
int check_address(size_t *array, listint_t *list, int size)
{
	int i;

	if (list == NULL || array == NULL)
		return (0);
	for (i = 0; i < size; i++)
	{
		if (array[i] == (size_t)list)
			return (1);
	}
	return (0);
}
