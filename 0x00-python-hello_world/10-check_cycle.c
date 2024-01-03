#include "lists.h"

/**
 * check_cycle - check if a cycle exists
 * @list: Linked list
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *temp, *notMove;

	temp = list;
	notMove = list;

	while (temp->next)
	{
		if (temp->next == NULL)
			return (0);
		temp = temp->next;
		if (temp->next == notMove)
			return (1);
	}

	return (0);
}
