#bisection

pick interval (a, b) over which to find minimum
pick tolerance (t)
while f(c) - f(a) > t or f(c) > t do
    evaluate function at a midpoint of inteval (a, b)
    set a and b to (a, c) or (c, a) such that interval contains zero
end while

bound so + and - (IMPORTANT - needs a smooth function that actually passes
        through zero)
cut in half, find the bound that crosses zero
rinse, repeat
stop when within tolerance

def tester(x)
    return(x**3 - 2x + 3)

#bonus?

#dj MCMC

choose parameters (x)
for all temp (t) values do
    randomly draw new parameters (y)
    val <- f(y)
    if runif(0, 1) <= val then
        x <- y
    end if
end for


