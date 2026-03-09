From Stdlib Require Import Arith.
Import Nat Peano.
From Stdlib Require Import Lia.
From Stdlib Require Import PeanoNat.

Theorem S_plus1 : forall n, S n = n + 1.
Proof.
  Search (_ + _) S plus.
  intros n.
  now rewrite add_1_r.
Qed.


Theorem lt_S_r : forall m n, m < S n -> m = n \/ m < n.
Proof.
  intros m n H.
  unfold lt in H.
  Search (S _ <= S _).
  About le_S_n.
  apply le_S_n in H.
  Search (_ <= _) "\/".
  About le_lteq.
  Search (_ \/ _).
  rewrite le_lteq in H.
  now apply or_comm in H.
Qed.

(** Определим функцию [sum : nat -> nat], такую что
[sum n = 1 + 2 + ... + n], и докажем, что [2 * sum n = n * (n + 1)]. *)

Fixpoint sum (n : nat) : nat :=
match n with
| 0 => 0
| S k => (sum k) + k + 1
end.

Compute sum 4.

Theorem sum_all_lia : forall n, 2 * sum n = n * (n + 1).
Proof.
  intros n.
  induction n as [| n IH]; [reflexivity |].
  simpl. Search (_ + 0). rewrite add_0_r.
  Search "plus". rewrite plus_n_Sm.
  replace (sum n + n + 1) with (sum n + (n + 1)) by lia.
  lia.
Qed.

Theorem sum_all : forall n, 2 * sum n = n * (n + 1).
Proof.
  intros n.
  induction n as [| k IH]; [reflexivity |].
  simpl. Search (_ + 0). rewrite add_0_r.
  replace (sum k + k + 1 + (sum k + k + 1)) with (2 * sum k + 2 * (k + 1)) by lia.
  rewrite IH. rewrite (mul_succ_r k (k + 1)).
  rewrite (S_plus1 (k + 1 + (k * (k + 1) + k))).
  simpl.
  rewrite add_0_r.
  replace (k + 1 + (k * (k + 1) + k) + 1) with (k * (k + 1) + (k + 1 + (k + 1))) by lia.
  reflexivity.
Qed.

(** 3. Определите функцию [sumOdd : nat -> nat], такую что
[sumOdd n = 1 + 3 + 5 + ... + (2n - 1)], и докажите, что
[sumOdd n = n * n]. *)

Fixpoint sumOdd (n : nat) : nat :=
  match n with
  | 0 => 0
  | S k => (sumOdd k) + 2 * k + 1
end.

Compute sumOdd 3.

Theorem sumOdd_all : forall n, sumOdd n = n * n.
Proof.
  intros n.
  induction n as [| k IH]; [reflexivity |].
  simpl.
  rewrite add_0_r. rewrite IH. rewrite mul_succ_r.
  replace (k * k + (k + k)) with (k + (k * k + k)) by lia.
  rewrite <- S_plus1. reflexivity.
Qed.

(** 4. Определите функцию [sumSquares : nat -> nat], такую что
[sumSquares n = 1 + 4 + 9 + ... + n^2], и докажите, что
[6 * sumSquares n = n * (n+1) * (2*n+1)]. *)

Fixpoint sumSquares (n : nat) : nat :=
  match n with
  | 0 => 0
  | S k => (sumSquares k) + (k + 1) * (k + 1)
end.

Compute sumSquares 3.

Theorem sumSquares_all : forall n, 6 * sumSquares n = n * (n + 1) * (2 * n + 1).
Proof.
  intros n.
  induction n as [| k IH]; [reflexivity |].
  simpl.
  lia.
Qed.


(** 5. Определите функцию [sumCubes : nat -> nat], такую что
[sumCubes n = 1 + 8 + 27 + ... + n^3], и докажите, что
[sumCubes n = (sum n)^2]. *)

Fixpoint sumCubes (n : nat) : nat :=
  match n with
  | 0 => 0
  | S k => (sumCubes k) + (k + 1) * (k + 1) * (k + 1)
end.

Compute sumCubes 3.

Theorem sumCubes_all : forall n, sumCubes n = (sum n)^2.
Proof.
  intros n.
  induction n as [| k IH]; [reflexivity |].
  simpl. rewrite IH. rewrite mul_1_r.

  replace ((sum k + k + 1) * (sum k + k + 1))
  with (sum k * sum k + 2 * sum k * (k + 1) + (k + 1) * (k + 1)) by ring.
  simpl. rewrite mul_1_r. rewrite add_0_r.
  About add_cancel_l.
  replace (sum k * sum k + (sum k + sum k) * (k + 1) + (k + 1) * (k + 1)) with
    (sum k * sum k + ((sum k + sum k) * (k + 1) + (k + 1) * (k + 1))) by ring.
  rewrite add_cancel_l with (p := sum k * sum k).

  replace (sum k + sum k) with
    (2 * sum k) by ring.

  rewrite sum_all.
  lia.
Qed.
