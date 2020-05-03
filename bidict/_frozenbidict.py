# -*- coding: utf-8 -*-
# Copyright 2009-2020 Joshua Bronson. All Rights Reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


#==============================================================================
#                    * Welcome to the bidict source code *
#==============================================================================

# Doing a code review? You'll find a "Code review nav" comment like the one
# below at the top and bottom of the most important source files. This provides
# a suggested initial path through the source when reviewing.
#
# Note: If you aren't reading this on https://github.com/jab/bidict, you may be
# viewing an outdated version of the code. Please head to GitHub to review the
# latest version, which contains important improvements over older versions.
#
# Thank you for reading and for any feedback you provide.

#                             * Code review nav *
#==============================================================================
# ← Prev: _base.py         Current: _frozenbidict.py           Next: _mut.py →
#==============================================================================

"""Provide :class:`frozenbidict`, an immutable, hashable bidirectional mapping type."""

from collections.abc import ItemsView
from typing import cast

from ._base import BidictBase, KT, VT
from ._delegating import _DelegatingMixin


class frozenbidict(_DelegatingMixin[KT, VT], BidictBase[KT, VT]):  # type: ignore
    """Immutable, hashable bidict type."""

    __slots__ = ()

    def __hash__(self) -> int:
        """The hash of this bidict as determined by its items."""
        if getattr(self, '_hash', None) is None:
            # pylint: disable=attribute-defined-outside-init
            self._hash = ItemsView(self)._hash()  # type: ignore
        return self._hash

    @property
    def inverse(self: 'frozenbidict[KT, VT]') -> 'frozenbidict[VT, KT]':
        """Overridden only to refine the type hint.

        Ref: https://github.com/python/typing/issues/548
        """
        return cast(frozenbidict[VT, KT], super().inverse)


#                             * Code review nav *
#==============================================================================
# ← Prev: _base.py         Current: _frozenbidict.py           Next: _mut.py →
#==============================================================================
