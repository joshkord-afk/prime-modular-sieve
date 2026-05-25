# Cross-Modular Sieve & Quadratic Diophantine Factorization Engine

A high-performance mathematical engine implemented in vanilla JavaScript and Python for fast prime generation and integer factorization on low-spec/constrained environments.

## Abstract
This project presents an optimized hybrid architecture that resolves two classic number theory problems in computer science: consecutive prime generation without memory-leakage or thread-freezing in client-side web environments, and fast integer factorization utilizing a quadratic Diophantine equation derived from three-term prime arithmetic progressions. 

By applying a **Cross-Modular Sieve** at the hardware-arithmetic level ($O(1)$ complexity), the engine filters out **99.81% of composite candidates** before invoking the costly Miller-Rabin primality test. Furthermore, the factorization engine bypasses trial division entirely, resolving prime factors $p_1, p_2$ of a composite $N$ in microsecond scale by locating a perfect square in the curve $C^2 + 8N = Y^2$.

---

## 1. Mathematical Architecture & Proofs

### A. The Two-Phase Prime Generator
Traditional prime generation algorithms are either memory-heavy (Sieve of Eratosthenes) or CPU-heavy (sequential primality testing). This engine decouples the process into two phases:

1. **Phase 1 (Combinatorial Pre-Population):** Creates a high-speed prime cache by evaluating quadratic and linear equations on a small seed list ($[2, 3, 5, 7]$) in $O(N^2)$ complexity.
2. **Phase 2 (Exhaustive Linear Consumer):** A sequential scanner ($2, 3, 4, \dots$) that checks primality. It achieves $O(1)$ performance in 95% of cases by verifying hits directly against the pre-populated cache.

### B. The Cross-Modular Sieve (Filtering Composites in $O(1)$)
When generating candidates $C_x$ from combinations of known primes $p_1, p_2$, the system evaluates:
* $C_1 = 2p_1 + p_2$
* $C_2 = 2p_1 - p_2$
* $C_3 = p_1 + p_2 - 1$
* $C_4 = p_1 \cdot p_2 - 2$
* $C_5 = p_1 \cdot p_2 + 2$

Instead of running Miller-Rabin on composites, we apply modular congruence filters derived from divisibility rules. For a prime control sieve $q \in \{3, 5, 7, 11, 13, 17, 19, 23, 29, 31\}$, a candidate is proven composite deterministically if:
* **For $C_1$:** $p_2 \equiv q - (2p_1 \pmod q) \pmod q$
* **For $C_2$:** $p_2 \equiv 2p_1 \pmod q$
* **For $C_3$:** $p_2 \equiv 1 - p_1 \pmod q$
* **For $C_4$:** $p_1 \cdot p_2 \equiv 2 \pmod q$
* **For $C_5$:** $p_1 \cdot p_2 \equiv q - 2 \pmod q$

Evaluating `(2 * p1) % q === p2 % q` runs in CPU-register scale, bypassing exponentiation entirely.

### C. Quadratic Diophantine Factorization ($C^2 + 8N = Y^2$)
Given a composite number $N = p_1 \cdot p_2$ (where $p_1, p_2$ are unknown prime factors):
We define the linear arithmetic progression difference variable $C = 2p_1 - p_2$. Multiplying by $p_1$:
$$p_1 \cdot C = 2p_1^2 - p_1 \cdot p_2$$

Substituting $p_1 \cdot p_2 = N$, we obtain the quadratic equation:
$$2p_1^2 - C \cdot p_1 - N = 0$$

Solving for $p_1$:
$$p_1 = \frac{C \pm \sqrt{C^2 + 8N}}{4}$$

For $p_1$ to be an integer factor, the discriminant must be a perfect square $Y^2$:
$$C^2 + 8N = Y^2$$

By iterating over odd integers $C$, once a perfect square $Y^2$ is found, the factors are resolved instantly as:
$$p_1 = \frac{Y + C}{4}$$
$$p_2 = \frac{Y - C}{2}$$

---

## 2. Empirical Benchmarks (First 200 Primes)
Evaluated on a dataset up to $N = 1223$:

* **Composite candidates generated:** $14,940$
* **Composites filtered by congruences in $O(1)$:** $14,912$
* **Fugitive composites requiring Miller-Rabin:** $28$
* **Sieve Accuracy:** **99.81%**
* **Factorization Speed ($N = 2,021,027$):** **0.000 ms** (8 iterations of $C$)

---

## 3. Repository Structure
* `index.html`: Web-based dashboard featuring the *Glassmorphism* UI, Prime Generator, and the Real-Time Factorizer.
* `scratch/criba_modular.py`: Performance simulation script for modular residue evaluations.
* `scratch/factorizacion_con_ecuacion.py`: Python CLI implementation of the Diophantine factorization.

## 4. Replication & Usage
1. Clone the repository.
2. Open `index.html` in any web browser to execute the generator or factorizer.
3. Run the python scripts in the `scratch/` folder to replicate the raw mathematical benchmarks.
