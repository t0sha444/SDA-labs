#include <stdio.h>
#include <stdlib.h>

/* A singly linked node shared by the stack and queue. */
typedef struct Node {
    int value;
    struct Node *next;
} Node;

/* ---------------- Stack: Last In, First Out ---------------- */
typedef struct {
    Node *top;
} Stack;

void stack_init(Stack *stack) {
    stack->top = NULL;
}

int stack_is_empty(const Stack *stack) {
    return stack->top == NULL;
}

int stack_push(Stack *stack, int value) {
    Node *node = malloc(sizeof(*node));
    if (node == NULL) return 0;
    node->value = value;
    node->next = stack->top;
    stack->top = node;
    return 1;
}

/* Returns 1 when a value was removed, 0 when the stack is empty. */
int stack_pop(Stack *stack, int *value) {
    if (stack_is_empty(stack)) return 0;
    Node *removed = stack->top;
    *value = removed->value;
    stack->top = removed->next;
    free(removed);
    return 1;
}

/* Returns 1 when a value is available, 0 when the stack is empty. */
int stack_peek(const Stack *stack, int *value) {
    if (stack_is_empty(stack)) return 0;
    *value = stack->top->value;
    return 1;
}

void stack_clear(Stack *stack) {
    int ignored;
    while (stack_pop(stack, &ignored)) {
        /* stack_pop frees each removed node */
    }
}

/* ---------------- Queue: First In, First Out ---------------- */
typedef struct {
    Node *front_node;
    Node *rear;
} Queue;

void queue_init(Queue *queue) {
    queue->front_node = NULL;
    queue->rear = NULL;
}

int queue_is_empty(const Queue *queue) {
    return queue->front_node == NULL;
}

int queue_enqueue(Queue *queue, int value) {
    Node *node = malloc(sizeof(*node));
    if (node == NULL) return 0;
    node->value = value;
    node->next = NULL;

    if (queue_is_empty(queue)) {
        queue->front_node = node;
    } else {
        queue->rear->next = node;
    }
    queue->rear = node;
    return 1;
}

/* Returns 1 when a value was removed, 0 when the queue is empty. */
int queue_dequeue(Queue *queue, int *value) {
    if (queue_is_empty(queue)) return 0;
    Node *removed = queue->front_node;
    *value = removed->value;
    queue->front_node = removed->next;
    if (queue->front_node == NULL) queue->rear = NULL;
    free(removed);
    return 1;
}

/* Returns 1 when a value is available, 0 when the queue is empty. */
int queue_front(const Queue *queue, int *value) {
    if (queue_is_empty(queue)) return 0;
    *value = queue->front_node->value;
    return 1;
}

void queue_clear(Queue *queue) {
    int ignored;
    while (queue_dequeue(queue, &ignored)) {
        /* queue_dequeue frees each removed node */
    }
}

/* ---------------- Tests required by Lab 2 ---------------- */
static void test_stack(void) {
    Stack stack;
    int value;
    stack_init(&stack);

    printf("STACK TESTS\n");
    printf("Initially empty: %s\n", stack_is_empty(&stack) ? "yes" : "no");
    printf("Pop empty stack: %s\n", stack_pop(&stack, &value) ? "unexpected value" : "handled");
    printf("Peek empty stack: %s\n", stack_peek(&stack, &value) ? "unexpected value" : "handled");

    stack_push(&stack, 9);
    if (stack_peek(&stack, &value)) printf("Peek one value: %d\n", value);
    if (stack_pop(&stack, &value)) printf("Pop one value: %d\n", value);

    stack_push(&stack, 4);
    stack_push(&stack, 7);
    stack_push(&stack, 2);
    printf("Pop order for 4, 7, 2: ");
    while (stack_pop(&stack, &value)) printf("%d ", value);
    printf("\nEmpty after removals: %s\n", stack_is_empty(&stack) ? "yes" : "no");

    stack_push(&stack, 5);
    if (stack_pop(&stack, &value)) printf("Can add again after emptying: %d\n\n", value);
    stack_clear(&stack);
}

static void test_queue(void) {
    Queue queue;
    int value;
    queue_init(&queue);

    printf("QUEUE TESTS\n");
    printf("Initially empty: %s\n", queue_is_empty(&queue) ? "yes" : "no");
    printf("Dequeue empty queue: %s\n", queue_dequeue(&queue, &value) ? "unexpected value" : "handled");
    printf("Front empty queue: %s\n", queue_front(&queue, &value) ? "unexpected value" : "handled");

    queue_enqueue(&queue, 9);
    if (queue_front(&queue, &value)) printf("Front one value: %d\n", value);
    if (queue_dequeue(&queue, &value)) printf("Dequeue one value: %d\n", value);

    queue_enqueue(&queue, 4);
    queue_enqueue(&queue, 7);
    queue_enqueue(&queue, 2);
    printf("Dequeue order for 4, 7, 2: ");
    while (queue_dequeue(&queue, &value)) printf("%d ", value);
    printf("\nEmpty after removals: %s\n", queue_is_empty(&queue) ? "yes" : "no");

    queue_enqueue(&queue, 5);
    if (queue_dequeue(&queue, &value)) printf("Can add again after emptying: %d\n\n", value);
    queue_clear(&queue);
}

int main(void) {
    test_stack();
    test_queue();
    return 0;
}
