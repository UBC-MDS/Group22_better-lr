# lr_plotting.py
# author: Jing Wen
# date: 2024-01-11

def plot_lr(X, y, intercept, coef, plot_to):
    """Visualize the "lr_cd" linear regression model.

    This function takes actual data points and an estimated regression line,
    displaying them together in a scatter plot. The plot is also
    saved as a PNG image.
    
    Parameters
    ----------
    X: ndarray
        The observed data 'x', the independent variable
    
    y: ndarray
       The observed data 'y', the dependent variable. Both 'x' and 'y' should be continuous and of the same length.

    intercept: float
        Optimized intercept generated by 'lr_cd' function. 
        It will be used to calculate the estimated values using observed data 'x'.
    
    coef: ndarray
        Optimized coefficient weights vector.
        It will be used to calculate the estimated values using observed data 'x'.
    
    plot_to : str
        A string representing the path to the directory where the plot will be saved.

    Returns
    -------
        A scatter plot of the observed data points overlayed with a line coming from the fitted weights.

    Examples
    --------
    >>> from lr_cd.lr_plotting import plot_lr
    >>> X = array([ 1.2390575 ,  1.99411649,  2.58284984,  2.37416463,  1.82673695,
    ...             1.71754177,  1.150911  ,  1.05020832, -0.28251291, -0.40102325])
    >>> y = array([ 2.3456723 ,  0.98456123,  3.1457892 ,  1.98765432,  2.9087645 ,
                    2.1345678 ,  0.12345678,  2.3456789 , -1.23456789, -0.12345678])
    >>> intercept = 0.42167642
    >>> coef = array([1.88190714])
    >>> plot_to = "results/figures"
    >>> plot_lr(X, y, intercept, coef, plot_to)
    """
    