# Attractors

This repos allows you to create beautiful pictures of the `Clifford` and `Peter de Jong` attractors using the `datashader` package.

![Attractor](images/Attractor.png)

## Running the code

To run the code, you need to install the required packages. You can do this by creating a new condat environment using the `environment.yml` file provided in the repo.

To generate some trajectories, you can simply run the `attractor.py` script
```bash
python attractor.py -A PeterdeJong -N 10000000 -C [1.4,-2.3,2.4,-2.1]
```
which will generate 10 million points for the Peter de Jong attractor with the parameters `(a, b, c, d) = (1.4, -2.3, 2.4, -2.1)` and dump then into a csv file.

If you want to play around with the parameters, datashader and visual, you can use the `Attractor-Datashader.ipynb` notebook.

### Clifford

Some interesting patterns can be obtained using this range of parameters

```
    (a, b, c, d) = (-1.4,  1.6,  1.0,  0.7)
                 = (-1.8, -2.0, -0.5, -0.9)
                 = ( 1.7,  1.7,  0.6,  1.2)
                 = ( 1.5, -1.8,  1.6,  0.9)
                 = (-1.7,  1.8, -1.9, -0.4)
```

### Peter de Jong 

```
    (a, b, d, c) = ( 1.40, -2.30, 2.40, -2.10)
                   ( 2.01, -2.53, 1.61, -0.33)
                   (-0.709,1.638, 0.452, 1.740)
                   (-2.00, -2.00, -1.20, 2.00)
```