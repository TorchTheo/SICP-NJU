;; Scheme ;;

(define (over-or-under a b)
  'YOUR-CODE-HERE
  (cond 
    ((> a b) 1)
    ((< a b) -1)
    ((= a b) 0)
  )
)

;;; Tests
(over-or-under 1 2)
; expect -1
(over-or-under 2 1)
; expect 1
(over-or-under 1 1)
; expect 0

(define (filter-lst fn lst)
  (cond ((null? lst) '())
        ((fn (car lst)) (cons (car lst) (filter-lst fn (cdr lst))))
        (else (filter-lst fn (cdr lst)))
)
)

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)

(define (make-adder n)
  (lambda (x) (+ n x))
)

;;; Tests
(define adder (make-adder 5))
(adder 8)
; expect 13

(define (no-repeats s)
  (if (null? s) s
    (cons (car s)
      (no-repeats (filter (lambda (x) (not (= (car s) x))) (cdr s)))))
)

(define (substitute s old new)

    (if (null? s) 
      s
      (if (pair? (car s))
        (cons (substitute (car s) old new) (substitute (cdr s) old new))
        (if (eq? (car s) old) 
        (cons new (substitute (cdr s) old new)) 
        (cons (car s) (substitute (cdr s) old new)))))
      
)

(define (sub-all s olds news)
  (if (null? olds)
    s
    (sub-all (substitute s (car olds) (car news)) (cdr olds) (cdr news)))
)