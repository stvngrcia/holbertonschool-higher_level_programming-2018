#include "lists.h"
/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to pointer of the first node in listint_t list.
 * Return: 0 if not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *h;
	listint_t *tmp;
	listint_t *tmp2;

	if (head == NULL || *head == NULL)
		return (0);
	h = *head;
	tmp = *head;

	/*set tmp to the last node*/
	while (tmp->next != NULL)
		tmp = tmp->next;

	while (h != tmp)
	{
		tmp2 = h;
		if (h->n != tmp->n)
			return (0);
		/*Moving tmp2 to the node before tmp*/
		while (tmp2->next != tmp)
			tmp2 = tmp2->next;
		tmp = tmp2;
		if (h == tmp)
			break;
		h = h->next;
	}
	return (1);
}
