#include "lists.h"

/**
 * check_cycle - Checks if there is a loop in a linked list.
 * @list: A pointer to the head of the linked list.
 * Return: 0 if there is not a loop, 1 if there is a loop.
 */
int check_cycle(listint_t *list)
{
	listint_t *head;
	listint_t *tmp;

	head = list;
	tmp = list;

	while(tmp != NULL && head->next != NULL && head->next->next != NULL)
	{
		head = head->next->next;
		tmp = tmp->next;

		if (head == tmp)
			return (1);
	}

	return (0);
}
