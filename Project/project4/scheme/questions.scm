(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))


;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15
  (define (helper s index)
    (cond
      ( (null? s) nil )
      (else (cons (cons index (cons (car s) nil)) (helper (cdr s) (+ 1 index)) ))
    )
   )
   (helper s 0)
  )
  ; END PROBLEM 15

;; Problem 16

;; Merge two lists LIST1 and LIST2 according to COMP and return
;; the merged lists.
(define (merge comp list1 list2)
  ; BEGIN PROBLEM 16
  (define (help1 comp lst x)
    (cond
      ((null? lst) (cons x nil))
      ((not(comp (car lst) x)) (cons x lst))
      (else (cons (car lst) (help1 comp (cdr lst) x)))))
  (if (null? list2)
    list1
    (merge comp (help1 comp list1 (car list2)) (cdr list2))))
  ; END PROBLEM 16


(merge < '(1 5 7 9) '(4 8 10))
; expect (1 4 5 7 8 9 10)
(merge > '(9 7 5 1) '(10 8 4 3))
; expect (10 9 8 7 5 4 3 1)

;; Problem 17

(define (nondecreaselist s)
    ; BEGIN PROBLEM 17
(if (null? s)
	 	nil
		(begin
		 	(define last (nondecreaselist (cdr s)))
			(define a (car s))
			(if (or (null? last) (> a (caar last)))
			 	(cons (cons a nil) last)
				(cons (cons a (car last)) (cdr last))
			)
		)
	)
)
    ; END PROBLEM 17


