
nums = sapply(d, is.numeric)
numeric.d = d[, nums]

large.nums = sapply(numeric.d, function (a) {max(a) > 10})
large.d = numeric.d[, large.nums]

