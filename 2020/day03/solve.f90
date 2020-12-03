program toboggan
    implicit none
    integer, parameter :: w = 31
    integer, parameter :: h = 323

    integer :: x, y
    character(len = w) :: row
    integer(kind=4), dimension(h) :: slope
    integer(kind=8) :: hit

    ! parse the slope
    do y = 1, h
        read(*,*) row
        do x = 1, w
            if (row(x:x) == '#') then
                slope(y) = ibset(slope(y), x - 1)
            else
                slope(y) = ibclr(slope(y), x - 1)
            end if
        end do
    end do

    ! part 1
    hit = trees(3, 1)
    write(*,*) hit

    ! part2
    hit = trees(1, 1)
    hit = hit * trees(3, 1)
    hit = hit * trees(5, 1)
    hit = hit * trees(7, 1)
    hit = hit * trees(1, 2)
    write(*,*) hit

contains

    function trees(dx, dy)
        implicit none
        integer :: trees, dx, dy
        integer :: x, y

        x = 0
        y = 1
        trees = 0

        do while (y <= h)
            if (btest(slope(y), x)) then
                trees = trees + 1
            end if
            x = x + dx
            y = y + dy
            x = mod(x, w)
       end do
    end function

end program
