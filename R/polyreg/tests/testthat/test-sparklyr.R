context("Sparklyr GLM data and model")

test_that("gen_dat_r has correct rows & columns",{
  df <- gen_df_sparklyr()
  expect_identical(colnames(df),c("x1","x2","x3","y"))
  expect_equal(sparklyr::sdf_nrow(df),10000) 
})

test_that("glm_r fits exact on no variance data",{
  df <- gen_df_sparklyr(B = c(4, 6, 2, -1), n = 10000, rng = c(-2, 4), err = c(0, 0))
  fit <- fit_sparklyr(df = df)
  coef<-c(4,6,2,-1)
  names(coef) <- c("(Intercept)","x1","x2","x3")
  expect_equal(round(fit$coefficients),coef)
})
