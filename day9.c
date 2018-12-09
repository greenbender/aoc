#include <stdio.h>
#include <stdlib.h>


typedef struct marble_t {
    struct marble_t *next, *prev;
    long value;
} marble_t;



static marble_t *anticlockwise(marble_t *self, int count) {
    if (!count)
        return self;
    return anticlockwise(self->prev, count - 1);
}


static marble_t *clockwise(marble_t *self, int count) {
    if (!count)
        return self;
    return clockwise(self->next, count - 1);
}


static marble_t *place(marble_t *self, marble_t *other) {
    other->prev = self;
    other->next = self->next;
    self->next->prev = other;
    self->next = other;
    return other;
}


static marble_t *pick(marble_t *self) {
    self->prev->next = self->next;
    self->next->prev = self->prev;
    return self->next;
}


#define max(a, b) ((a) > (b) ? a : b)


static long highest_score(int players, long last) {
    long i;
    int player = 0;
    long highest = 0;

    /* allocate and init scores */
    long *score = calloc(players, sizeof(*score));

    /* allocate all marbles at once */
    marble_t *marbles = malloc(last * sizeof(*marbles));
    marble_t *current = marbles;

    /* init first marble */
    current->prev = current->next = current;
    current->value = 0;
    
    for (i = 1; i < last; i++) {
        if (i % 23 == 0) {
            score[player] += i;
            current = anticlockwise(current, 7);
            score[player] += current->value;
            highest = max(highest, score[player]);
            current = pick(current);
        } else {
            current = clockwise(current, 1);
            current = place(current, &marbles[i]);
            current->value = i;
        }
        player = (player + 1) % players;
    }

    free(marbles);
    free(score);

    return highest;
}
            

int main(int argc, char **argv) {
    int players = atoi(argv[1]);
    long last = strtol(argv[2], NULL, 0) + 1;
    printf("%ld\n", highest_score(players, last));
    return 0;
}
