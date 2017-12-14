#include "lists.h"
int palindrome(listint_t **head, listint_t *end);
/**
 *
 *
 *
 */
int is_palindrome(listint_t **head)
{
	int val;

	val = palindrome(head, *head);

	return (val);
}

int palindrome(listint_t **head, listint_t *end)
{
	int i;

	if (end == NULL)
		return (1);
	i = palindrome(head, end->next);

	if ((*head)->n == end->n && i != 0)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
