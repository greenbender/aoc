#include <string.h>
#include <stdio.h>
#include <stdlib.h>


struct state_t {
    char *data;
    size_t len;
    size_t size;
    int elf0;
    int elf1;
} state;


void state_init(void) {
    state.data = malloc(1024 * 1024);
    state.size = 1024 * 1024;
    state.elf0 = 0;
    state.elf1 = 1;
    state.data[state.elf0] = '3';
    state.data[state.elf1] = '7';
    state.len = 2;
    
}


void state_cleanup(void) {
    free(state.data);
}


void state_update(void) {
    char r0 = state.data[state.elf0] ^ 0x30;
    char r1 = state.data[state.elf1] ^ 0x30;
    char c = r0 + r1;
    char c0 = c / 10;
    char c1 = c % 10;

    if (state.len + 2 > state.size) {
        state.size += state.size << 1;
        state.data = realloc(state.data, state.size);
    }

    if (c0)
        state.data[state.len++] = c0 | 0x30;
    state.data[state.len++] = c1 | 0x30;

    state.elf0 = (state.elf0 + r0 + 1) % state.len;
    state.elf1 = (state.elf1 + r1 + 1) % state.len;
}


int main(int argc, char **argv) {
    long end = strtol(argv[1], NULL, 0);
    char *sequence = argv[1];
    size_t len = strlen(sequence);

    state_init();

    /* part 1 */
    do {
        state_update();
    } while (state.len < end + 10);
    printf("%s\n", &state.data[state.len - 10]);

    /* part 2 */
    while (1) {
        state_update();
        if (memcmp(&state.data[state.len - len - 1], sequence, len) == 0) {
            printf("%lu\n", state.len - 7);
            break;
        } else if (memcmp(&state.data[state.len - len], sequence, len) == 0) {
            printf("%lu\n", state.len - 6);
            break;
        }
    }

    state_cleanup();

    return 0;
}
