#include <stdio.h>
#include <stdlib.h>
#include "queue.h"

Queue newQueue() {
	Queue q = (Queue) malloc(sizeof(Queue*));
	if (q == NULL) {
		   printf("Memory request denied\n");
		   exit(1);
	}
	q->first = NULL;
	q->current = NULL;
	q->last = NULL;
	return q;
}

void enqueue(Queue q, QueueData it) {
	queueElem *qe = (queueElem *) malloc(sizeof(queueElem));
	qe->item = it;
	qe->next = NULL;
	if (q->first == NULL) {
		q->first = qe;
		q->current = qe;
		q->last = qe;
		return;
	}
	(q->last)->next = qe;
	q->last = (q->last)->next;
	return;
}

QueueData dequeue(Queue q) {
	if (q == NULL)
		return NULL;
	if (q->current == q->first) {
		q->current = (q->first)->next;
	}
	queueElem *qp = q->first;
	QueueData data = qp->item;
	q->first = (q->first)->next;
	free(qp);
	return data;
}

QueueData first(Queue q) {
	if (q == NULL)
		return NULL;
	return q->first;
}

int qLength(Queue q) {
	if (q == NULL)
		return 0;
	int i = 0;
	while(qitMore(q)) {
		qitNext(q);
		i++;
	}
	qitReset(q);
	return i;
}

void qitReset(Queue q) {
	q->current = q->first;
	return;
}

int qitMore(Queue q) {
	if (q->current == NULL)
		return 0;
	else
		return 1;
}

QueueData qitNext(Queue q) {
	if (qitMore(q)) {
		queueElem *qe = q->current;
		q->current = (q->current)->next;
		return qe->item;
	} else {
		return NULL;
	}
}