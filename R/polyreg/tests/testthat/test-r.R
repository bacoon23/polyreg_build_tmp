context("Local GLM data and model")

test_that("gen_dat_r has correct rows & columns",{
  dat <- gen_dat_r()
  expect_identical(ls(dat),c("x1","x2","x3","y"))
  expect_equal(nrow(dat),10000) 
})

test_that("glm_r fits exact on no variance data",{
  dat <- gen_dat_r(B = c(4, 6, 2, -1), n = 10000, rng = c(-2, 4), err = c(0, 0))
  lm <- glm_r(dat = dat)
  coef<-c(4,6,2,-1)
  names(coef) <- c("(Intercept)","x1","x2","x3")
  expect_equal(lm$coefficients,coef)
})
