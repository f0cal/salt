# -*- coding: utf-8 -*-
'''
Functions to view the minion's public key information
'''
from __future__ import absolute_import, unicode_literals, print_function

# Import python libs
import os

# Import Salt libs
import salt.utils.crypt


def finger(hash_type=None, tgt_pki_dir=None):
    '''
    Return the minion's public key fingerprint

    hash_type
        The hash algorithm used to calculate the fingerprint

    CLI Example:

    .. code-block:: bash

        salt '*' key.finger
    '''
    if hash_type is None:
        hash_type = __opts__['hash_type']

    if tgt_pki_dir is None:
        tgt_pki_dir = __opts__['pki_dir']

    pki_path = os.path.join(tgt_pki_dir, 'minion.pub')
    return salt.utils.crypt.pem_finger(pki_path, sum_type=hash_type)


def finger_master(hash_type=None):
    '''
    Return the fingerprint of the master's public key on the minion.

    hash_type
        The hash algorithm used to calculate the fingerprint

    CLI Example:

    .. code-block:: bash

        salt '*' key.finger_master
    '''
    if hash_type is None:
        hash_type = __opts__['hash_type']

    return salt.utils.crypt.pem_finger(
        os.path.join(__opts__['pki_dir'], 'minion_master.pub'),
        sum_type=hash_type)
