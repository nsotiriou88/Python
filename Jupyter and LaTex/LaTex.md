
#Tutorial Brief

**Video Tutorial:** https://www.youtube.com/user/roshanRush

Jupyter has an implementation of markdown language that can be used in in markdown cells to create formatted text and media documentation in your notebook. LaTeX is also implemented to create high quality mathematical typeset.

#Markdown

##Headings

#H1
##H2
###H3
####H4
#####H5
######H6

**Code:**
```markdown
#H1
##H2
###H3
####H4
#####H5
######H6
```

##Alternative Headings

Heading 1
=========

Heading 2
----------

**Code:**
```markdown
Heading 1
=========

Heading 2
---------
```

##Font Styles

**Bold Font** or __Bold Font__

*Italic* or _Italic Font_

~~Scratched Text~~

Markdown doesn't support underline. but you can do that using HTML <u>Text</u>

**Code:**
```markdown
**Bold Font** or __Bold Font__

*Italic* or _Italic Font_

~~Scratched Text~~

Markdown doesn't support underline. but you can do that using HTML <u>Text</u>
```

##Lists

- item
- item
 - subitem
 - subitem
- item


1. item
2. item
 1. sub item
 2. sub item
3. item

**Code:**
```markdown
- item
- item
 - subitem
 - subitem
- item


1. item
2. item
 1. sub item
 2. sub item
3. item
```

##Links

http://www.github.com/

[Github](http://www.github.com/)


**Code:**
```
http://www.github.com/

[Github](http://www.github.com/)
```

##Images
![Turing's Device](http://www.google.com/logos/2012/turing-doodle-static.jpg "Alan Turing's 100th Birthday")

**Code:**
```markdown
![Turing's Device](http://www.google.com/logos/2012/turing-doodle-static.jpg "Alan Turing's 100th Birthday")
```

##Quotes

> Why, oh why, Javascript??? Wars, famine, planetary destruction... I guess as a species, we deserve this abomination...
>
> [Fernando Perez](https://twitter.com/fperez_org)

**Code:**
```
> Why, oh why, Javascript??? Wars, famine, planetary destruction... I guess as a species, we deserve this abomination...
>
> [Fernando Perez](https://twitter.com/fperez_org)
```

##Horizontal Line

---

**Code:**
```markdown
---
```

##Tables

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned |  1600 |
| col 2 is      | centered      |    12 |
| zebra stripes | are neat      |     1 |

**Code:**

```
| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned |  1600 |
| col 2 is      | centered      |    12 |
| zebra stripes | are neat      |     1 |
```

##HTML

<b>You</b> can <i>render</i> almost any <span style="color:red;">HTML</span> code you <u>like</u>.

**Code:**

```
<b>You</b> can <i>render</i> almost any <span style="color:red;">HTML</span> code you <u>like</u>.
```

##Code

You can add in line code like this `import numpy as np`

Or block code:

Python Code:
```python
x = 5
print "%.2f" % x
```

Java Script Code:
```javascript
x = 5
alert(x);
```

**Code:**

<pre>
Python Code:
```python
x = 5
print "%.2f" % x
```

Java Script Code:
```javascript
x = 5
alert(x);
```
</pre>

#LaTeX

**References:**

- [LaTeX Wiki](http://en.wikibooks.org/wiki/LaTeX/Mathematics)
- [Duke University, Department of  Statistical Science](https://stat.duke.edu/resources/computing/latex)
- [Equation Sheet](http://www.equationsheet.com/)

LaTeX is a large typeset system for scientific documentation which symbols for mathematics, statistics, physics, quantum mechanics, and computer science. It is beyond the scope of this tutorial to cover everything, but we will go over the basics of writing high quality mathematical equations using LaTeX.

You can use LaTeX in line by like this $y = x^2$ or in block like this $$y = x^2$$

**Code:**
```markdown
You can use LaTeX in line by like this $y = x^2$ or in block like this $$y = x^2$$
```

##Operators:

- Add:
 - $x + y$
- Subtract:
 - $x - y$
- Multiply
 - $x * y$
 - $x \times y$ 
 - $x . y$ 
- Divide
 - $x / y$
 - $x \div y$
 - $\frac{x}{y}$

**Code:**
```markdown
- Add:
 - $x + y$
- Subtract:
 - $x - y$
- Multiply
 - $x * y$
 - $x \times y$ 
 - $x . y$ 
- Divide
 - $x / y$
 - $x \div y$
 - $\frac{x}{y}$
```

##Relations

- $\pi \approx 3.14159$
- ${1 \over 0} \neq \inf$
- $0 < x > 1$
- $0 \leq x \geq 1$

**Code:**
```
- $\pi \approx 3.14159$
- ${1 \over 0} \neq \inf$
- $0 < x > 1$
- $0 \leq x \geq 1$
```

##Fractions

- $^1/_2$
- $\frac{1}{2x}$
- ${3 \over 4}$


**Code:**
```
- $^1/_2$
- $\frac{1}{2x}$
- ${3 \over 4}$
```

##Greek Alphabet

| Small Letter          | Capical Letter       | Alervative                  |
| --------------------- | -------------------- | --------------------------- |
| $\alpha$   `\alpha`   | $A$ `A`              |                             |
| $\beta$   `\beta`     | $B$ `B`              |                             |
| $\gamma$   `\gamma`   | $\Gamma$ `\Gamma`    |                             |
| $\delta$   `\delta`   | $\Delta$ `\Delta`    |                             |
| $\epsilon$ `\epsilon` | $E$ `E`              | $\varepsilon$ `\varepsilon` |
| $\zeta$   `\zeta`     | $Z$ `Z`              |                             |
| $\eta$   `\eta`       | $H$ `H`              |                             |
| $\theta$ `\theta`     | $\Theta$ `\Theta`    | $\vartheta$ `\vartheta`     |
| $\iota$   `\zeta`     | $I$ `I`              |                             |
| $\kappa$ `\kappa`     | $K$ `K`              | $\varkappa$ `\varkappa`     |
| $\lambda$   `\lambda` | $\Lambda$ `\Lambda`  |                             |
| $\mu$   `\mu`         | $M$ `M`              |                             |
| $\nu$   `\nu`         | $N$ `N`              |                             |
| $\xi$   `\xi`         | $Xi$ `\Xi`           |                             |
| $\omicron$ `\omicron` | $O$ `O`              |                             |
| $\pi$ `\pi`           | $\Pi$ `\Pi`          | $\varpi$ `\varpi`           |
| $\rho$ `\rho`         | $P$ `P`              | $\varrho$ `\varrho`         |
| $\sigma$ `\sigma`     | $\Sigma$ `\Sigma`    | $\varsigma$ `\varsigma`     |
| $\tau$   `\tau`       | $T$ `T`              |                             |
| $\upsilon$ `\upsilon` | $\Upsilon$ `\Upsilon`|                             |
| $\phi$ `\phi`         | $\Phi$ `\Phi`        | $\varphi$ `\varphi`         |
| $\chi$   `\chi`       | $X$ `X`              |                             |
| $\psi$ `\psi`         | $\Psi$ `\Psi`        |                             |
| $\omega$   `\omega`   | $\Omega$ `\Omega`    |                             |

##Power & Index

You can add power using the carrot `^` symbol. If you have more than one character you have to enclose them in a curly brackets.

 $$f(x) = x^2 - x^{1 \over \pi}$$

For index you can use the underscore symbol:

$$f(X,n) = X_n + X_{n-1}$$

**Code:**
```markdown
$$f(x) = x^2 - x^{1 \over \pi}$$
$$f(X,n) = X_n + X_{n-1}$$

```

##Roots & Log

You can express a square root in LaTeX using the `\sqrt` and to change the level of the root you can use `\sqrt[n]` where `n` is the level of the root.

$$f(x) = \sqrt[3]{2x} + \sqrt{x-2}$$

To represent a log use `\log[base]` where `base` is the base of the logarithmic term.

$$\log[x] x = 1$$

**Code:**
```markdown
$$f(x) = \sqrt[3]{2x} + \sqrt{x-2}$$
```

##Sums & Products

You can represent a sum with a sigma using `\sum\limits_{a}^{b}` where a and b are the lower and higher limits of the sum.

$$\sum\limits_{x=1}^{\infty} {1 \over x} = 2$$

Also you can represent a product with `\prod\limits_{a}^{a}` where a and b are the lower and higher limits.

$$\prod\limits_{i=1}^{n} x_i - 1$$

**Code:**
```
$$\sum\limits_{x=1}^{\infty} {1 \over x} = 2$$
$$\prod\limits_{i=1}^{n} x_i - 1$$
```

##Statistics

To represent basic concepts in statistics about sample space `S`, you can represent a maximum:

$$max(S) = \max\limits_{i: S_i \in S} S_i$$

In the same way you can get the minimum:

$$min(S) = \min\limits_{i: S_i \in S} S_i$$

To represent a [binomial coefficient](http://en.wikipedia.org/wiki/Binomial_coefficient) with n choose k, use the following:

$$\frac{n!}{k!(n-k)!} = {n \choose k}$$

for :

**Code:**
```
$$max(S) = \max\limits_{i: x_i \in \{S\}} x_i$$
$$min (S) = \min\limits_{i: x_i \in \{S\}} x_i$$
$$\frac{n!}{k!(n-k)!} = {n \choose k}$$
```

##Calculus

Limits are represented using `\lim\limits_{x \to a}` as `x` approaches `a`.

$$\lim\limits_{x \to 0^+} {1 \over 0} = \infty$$

For integral equations use `\int\limits_{a}^{b}` where `a` and `b` are the lower and higher limits.

$$\int\limits_a^b 2x \, dx$$


**Code:**
```markdown
$$\lim\limits_{x \to 0^+} {1 \over 0} = \inf$$
$$\int\limits_a^b 2x \, dx$$
```

##Function definition over periods

Defining a function that is calculated differently over a number of period can done using LaTeX. There are a few tricks that we will use to do that:

- The large curly bracket `\left\{ ... \right.` Notice it you want to use `(` or `[` you don't have to add a back slash(`\`). You can also place a right side matching bracket by replacing the `.` after `\right` like this `.right}`
- Array to hold the definitions in place. it has two columns with left alignment. `\begin{array}{ll} ... \end{array}`
- Line Breaker `\\`
- Text alignment box ` \mbox{Text}`

$f(x) =\left\{\begin{array}{ll}0  & \mbox{if } x = 0 \\{1 \over x} & \mbox{if } x \neq 0\end{array}\right.$

**Code:**
```
$f(x) =
\left\{
	\begin{array}{ll}
		0  & \mbox{if } x = 0 \\
		{1 \over x} & \mbox{if } x \neq 0
	\end{array}
\right.$
```

**Note:** If you are planning to show your notebook in NBViewer write your latex code in one line. For example you can write the code above like this:

```
$f(x) =\left\{\begin{array}{ll}0  & \mbox{if } x = 0 \\{1 \over x} & \mbox{if } x \neq 0\end{array}\right.$
```

#Quick Quiz (Normal Distribution)

Try to replicate the [Normal Distribution](http://en.wikipedia.org/wiki/Normal_distribution) formula using LaTeX. If you solve it, leave the LaTeX code in the comments below. $Don't\ cheat$.

$$P(x,\sigma,\mu) = \frac{1}{{\sigma \sqrt {2\pi } }}e^{{-(x - \mu)^2 } / {2\sigma ^2}}$$

Tips to help with the quiz:

- $\mu$ is `\mu`
- $\sigma$ is `\sigma`
- $e$ is `e`
