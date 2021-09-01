
total_ticket = 0
student_ticket = 0
standard_ticket = 0
kids_ticket = 0

while True:
    movie = input()
    if movie == 'Finish':
        break
    free_space_cinema = int(input())
    free_space = free_space_cinema

    ticket_for_one_movie = 0

    while free_space > 0:
        ticket = input()
        if ticket == 'End':
            break
        if ticket == 'student':
            student_ticket += 1
        if ticket == 'standard':
            standard_ticket += 1
        if ticket == 'kid':
            kids_ticket += 1
        free_space -= 1
        total_ticket += 1
        ticket_for_one_movie += 1

    print(f"{movie} - {(ticket_for_one_movie / free_space_cinema) * 100:.2f}% full.")

print(f"Total tickets: {total_ticket}")
print(f"{(student_ticket / total_ticket) * 100:.2f}% student tickets.")
print(f"{(standard_ticket / total_ticket) * 100:.2f}% standard tickets.")
print(f"{(kids_ticket / total_ticket) * 100:.2f}% kids tickets.")