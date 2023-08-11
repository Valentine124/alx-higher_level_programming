#include "lists.h"

/**
 * check_cycle - check if linked list is a cycle
 * @list: the list
 *
 * Return: 1 if cycle or 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = list, *check = NULL;

	while (temp)
	{
		if (check == list)
			return (1);
		temp = temp->next;
		check = temp;
	}

	return (0);
}
