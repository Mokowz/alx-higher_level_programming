#include "lists.h"

/**
 * insert_node - insert node at a position
 * @head: First node
 * @number: Number to be inserted
 * Return: pointer or null
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	while (temp)
	{
		if (temp->n < number && temp->next->n > number)
		{
			new->next = temp->next;
			temp->next = new;
			return (new);
		}
		else if (temp->n < numbeer && temp->next == NULL)
		{
			temp->next = new;
			return (new);
		}
		temp = temp->next;
	}
	return (NULL);
}
