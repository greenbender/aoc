using DelimitedFiles


masses = readdlm(stdin, Int)


function fuel(mass::Int)::Int
    mass ÷ 3 - 2
end


function fuel_r(mass::Int)
    f = fuel(mass)
    f <= 0 ? 0 : f + fuel_r(f)
end


function part1()
    println(sum(fuel, masses))
end


function part2()
    println(sum(fuel_r, masses))
end


part1()
part2()
