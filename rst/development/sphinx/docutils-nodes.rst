DocUtils Nodes
##############

.. tikz:: An Example Directive with Caption

   \draw[thick,rounded corners=8pt]
   (0,0)--(0,2)--(1,3.25)--(2,2)--(2,0)--(0,2)--(2,2)--(0,0)--(2,0);

..  tikz::  Example UML Class

    \begin{class}[text width=8cm]{Node}{0,0}
        \attribute{parentname : Node = None}
        \attribute{document : Document = None}
        \attribute{source : str = None}
        \attribute{line : int = 0}

        \operation{traverse(parameter list) : type of value returned}
        % virtual operation
        \operation[0]{depart(parameters list) : type of value returned}
    \end{class}

And more text.

..  tikz::  logo

    \begin{class}[text width=5cm]{BankAccount}{0,0}
        \attribute{owner : String} \attribute{balance : Dollars = 0}
        \operation{deposit(amount : Dollars)}
        \operation[0]{withdrawl(amount : Dollars)}
    \end{class}
    \begin{class}[text width=7cm]{CheckingAccount}{-5,-5}
        \inherit{BankAccount}
        \attribute{insufficientFundsFee : Dollars}
        \operation{processCheck ( checkToProcess : Check )}
        \operation{withdrawal ( amount : Dollars )}
    \end{class}
    \begin{class}[text width=7cm]{SavingsAccount}{5,-5}
        \inherit{BankAccount}
        \attribute{annualInteresRate : Percentage}
        \operation{depositMonthlyInterest ( )} \operation{withdrawal ( amount : Dollars )}
    \end{class}

