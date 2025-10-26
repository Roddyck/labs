1. Рассмотрим определение\
(define (double f) (lambda (x) (f (f x))))\
Напишите $lambda$-терм, соответствующий double.\
Выполняя $beta$-редукции вручную, определите значение выражения\
(((double double) add1) 2)\

#let double = $lambda f x. f (f x)$
$
  "d" := #double
$

$
  d d a 2
$

$
  d g x ->^*_(beta) g (g x)
$

$
  d (d a) 2\
  d a (d a 2)\
  a (a (d a 2))\
  a (a (a (a (2))))
$

#let True = $lambda x y. x$
#let False = $lambda x y. y$
#let If = $lambda b x y. b x y$ 

$
  (#If) (#True) M N\
  -> (#True) M N
$
