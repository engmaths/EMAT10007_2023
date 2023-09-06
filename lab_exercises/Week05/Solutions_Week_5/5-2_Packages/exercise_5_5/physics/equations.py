if __name__ == '__main__':
    print('equations.py is being used as a script')
else:
    print('equations.py is being imported and used as a package/module')


def gravitation(G, m_1, m_2, r):
    """
    Defines Newton's law of gravitation
    """
    F = G * m_1 * m_2 / r**2
    return F


def mass_energy(m, c):
    """
    Defines Einstein's mass-energy formula
    """

    E = m * c**2
    return E
