import sys

import math as python_lib_Math
import math as Math
from os import path as python_lib_os_Path
import inspect as python_lib_Inspect
from docutils.frontend import OptionParser as docutils_frontend_OptionParser
from docutils.parsers.rst import Parser as docutils_parsers_rst_Parser
import docutils.utils as docutils_utils_Utils_Module
import importlib as importlib_Importlib_Module
import inspect as inspect_Inspect_Module
from inspect import Parameter as inspect_Parameter
import pkgutil as pkgutil_Pkgutil_Module
import re as python_lib_Re
import sys as python_lib_Sys
import builtins as python_lib_Builtins
import functools as python_lib_Functools
import json as python_lib_Json
try:
    import msvcrt as python_lib_Msvcrt
except:
    pass
import os as python_lib_Os
import random as python_lib_Random
import shutil as python_lib_Shutil
import subprocess as python_lib_Subprocess
try:
    import termios as python_lib_Termios
except:
    pass
import time as python_lib_Time
import timeit as python_lib_Timeit
import traceback as python_lib_Traceback
try:
    import tty as python_lib_Tty
except:
    pass
from datetime import datetime as python_lib_datetime_Datetime
from datetime import timedelta as python_lib_datetime_Timedelta
from datetime import tzinfo as python_lib_datetime_Tzinfo
from datetime import timezone as python_lib_datetime_Timezone
from io import IOBase as python_lib_io_IOBase
from io import BufferedIOBase as python_lib_io_BufferedIOBase
from io import RawIOBase as python_lib_io_RawIOBase
from io import FileIO as python_lib_io_FileIO
from io import TextIOBase as python_lib_io_TextIOBase
from io import StringIO as python_lib_io_StringIO
from json import JSONEncoder as python_lib_json_JSONEncoder
from time import struct_time as python_lib_time_StructTime
import urllib.parse as python_lib_urllib_Parse


class _hx_AnonObject:
    _hx_disable_getattr = False
    def __init__(self, fields):
        self.__dict__ = fields
    def __repr__(self):
        return repr(self.__dict__)
    def __contains__(self, item):
        return item in self.__dict__
    def __getitem__(self, item):
        return self.__dict__[item]
    def __getattr__(self, name):
        if (self._hx_disable_getattr):
            raise AttributeError('field does not exist')
        else:
            return None
    def _hx_hasattr(self,field):
        self._hx_disable_getattr = True
        try:
            getattr(self, field)
            self._hx_disable_getattr = False
            return True
        except AttributeError:
            self._hx_disable_getattr = False
            return False



_hx_classes = {}


class Enum:
    _hx_class_name = "Enum"
    __slots__ = ("tag", "index", "params")
    _hx_fields = ["tag", "index", "params"]
    _hx_methods = ["__str__"]

    def __init__(self,tag,index,params):
        self.tag = tag
        self.index = index
        self.params = params

    def __str__(self):
        if (self.params is None):
            return self.tag
        else:
            return self.tag + '(' + (', '.join(str(v) for v in self.params)) + ')'

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.tag = None
        _hx_o.index = None
        _hx_o.params = None
Enum._hx_class = Enum
_hx_classes["Enum"] = Enum


class Class: pass


class CompileTime:
    _hx_class_name = "CompileTime"
    __slots__ = ()
CompileTime._hx_class = CompileTime
_hx_classes["CompileTime"] = CompileTime


class CompileTimeClassList:
    _hx_class_name = "CompileTimeClassList"
    __slots__ = ()
    _hx_statics = ["__meta__", "lists", "get", "getTyped", "initialise"]

    @staticmethod
    def get(id):
        if (CompileTimeClassList.lists is None):
            CompileTimeClassList.initialise()
        return CompileTimeClassList.lists.h.get(id,None)

    @staticmethod
    def getTyped(id,_hx_type):
        return CompileTimeClassList.get(id)

    @staticmethod
    def initialise():
        CompileTimeClassList.lists = haxe_ds_StringMap()
        m = haxe_rtti_Meta.getType(CompileTimeClassList)
        if (Reflect.field(m,"classLists") is not None):
            _g = 0
            _g1 = Reflect.field(m,"classLists")
            while (_g < len(_g1)):
                item = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                array = item
                listID = (array[0] if 0 < len(array) else None)
                _hx_list = haxe_ds_List()
                _g2 = 0
                _this = (array[1] if 1 < len(array) else None)
                _g3 = _this.split(",")
                while (_g2 < len(_g3)):
                    typeName = (_g3[_g2] if _g2 >= 0 and _g2 < len(_g3) else None)
                    _g2 = (_g2 + 1)
                    _hx_type = Type.resolveClass(typeName)
                    if (_hx_type is not None):
                        _hx_list.push(_hx_type)
                CompileTimeClassList.lists.h[listID] = _hx_list
CompileTimeClassList._hx_class = CompileTimeClassList
_hx_classes["CompileTimeClassList"] = CompileTimeClassList


class Date:
    _hx_class_name = "Date"
    __slots__ = ("date", "dateUTC")
    _hx_fields = ["date", "dateUTC"]
    _hx_methods = ["getTime", "getHours", "getMinutes", "getSeconds", "getFullYear", "getMonth", "getDate", "getDay", "getUTCHours", "getUTCMinutes", "getUTCSeconds", "getUTCFullYear", "getUTCMonth", "getUTCDate", "getUTCDay", "getTimezoneOffset", "toString"]
    _hx_statics = ["now", "fromTime", "makeLocal", "UTC", "fromString"]

    def __init__(self,year,month,day,hour,_hx_min,sec):
        self.dateUTC = None
        if (year < python_lib_datetime_Datetime.min.year):
            year = python_lib_datetime_Datetime.min.year
        if (day == 0):
            day = 1
        self.date = Date.makeLocal(python_lib_datetime_Datetime(year,(month + 1),day,hour,_hx_min,sec,0))
        self.dateUTC = self.date.astimezone(python_lib_datetime_Timezone.utc)

    def getTime(self):
        return (self.date.timestamp() * 1000)

    def getHours(self):
        return self.date.hour

    def getMinutes(self):
        return self.date.minute

    def getSeconds(self):
        return self.date.second

    def getFullYear(self):
        return self.date.year

    def getMonth(self):
        return (self.date.month - 1)

    def getDate(self):
        return self.date.day

    def getDay(self):
        return HxOverrides.mod(self.date.isoweekday(), 7)

    def getUTCHours(self):
        return self.dateUTC.hour

    def getUTCMinutes(self):
        return self.dateUTC.minute

    def getUTCSeconds(self):
        return self.dateUTC.second

    def getUTCFullYear(self):
        return self.dateUTC.year

    def getUTCMonth(self):
        return (self.dateUTC.month - 1)

    def getUTCDate(self):
        return self.dateUTC.day

    def getUTCDay(self):
        return HxOverrides.mod(self.dateUTC.isoweekday(), 7)

    def getTimezoneOffset(self):
        x = (self.date.utcoffset() / python_lib_datetime_Timedelta(0,60))
        tmp = None
        try:
            tmp = int(x)
        except BaseException as _g:
            None
            tmp = None
        return -tmp

    def toString(self):
        return self.date.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def now():
        d = Date(2000,0,1,0,0,0)
        d.date = Date.makeLocal(python_lib_datetime_Datetime.now())
        d.dateUTC = d.date.astimezone(python_lib_datetime_Timezone.utc)
        return d

    @staticmethod
    def fromTime(t):
        d = Date(2000,0,1,0,0,0)
        d.date = Date.makeLocal(python_lib_datetime_Datetime.fromtimestamp((t / 1000.0)))
        d.dateUTC = d.date.astimezone(python_lib_datetime_Timezone.utc)
        return d

    @staticmethod
    def makeLocal(date):
        try:
            return date.astimezone()
        except BaseException as _g:
            None
            tzinfo = python_lib_datetime_Datetime.now(python_lib_datetime_Timezone.utc).astimezone().tzinfo
            return date.replace(**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'tzinfo': tzinfo})))

    @staticmethod
    def UTC(year,month,day,hour,_hx_min,sec):
        return (python_lib_datetime_Datetime(year,(month + 1),day,hour,_hx_min,sec,0,python_lib_datetime_Timezone.utc).timestamp() * 1000)

    @staticmethod
    def fromString(s):
        _g = len(s)
        if (_g == 8):
            k = s.split(":")
            return Date.fromTime((((Std.parseInt((k[0] if 0 < len(k) else None)) * 3600000.) + ((Std.parseInt((k[1] if 1 < len(k) else None)) * 60000.))) + ((Std.parseInt((k[2] if 2 < len(k) else None)) * 1000.))))
        elif (_g == 10):
            k = s.split("-")
            return Date(Std.parseInt((k[0] if 0 < len(k) else None)),(Std.parseInt((k[1] if 1 < len(k) else None)) - 1),Std.parseInt((k[2] if 2 < len(k) else None)),0,0,0)
        elif (_g == 19):
            k = s.split(" ")
            _this = (k[0] if 0 < len(k) else None)
            y = _this.split("-")
            _this = (k[1] if 1 < len(k) else None)
            t = _this.split(":")
            return Date(Std.parseInt((y[0] if 0 < len(y) else None)),(Std.parseInt((y[1] if 1 < len(y) else None)) - 1),Std.parseInt((y[2] if 2 < len(y) else None)),Std.parseInt((t[0] if 0 < len(t) else None)),Std.parseInt((t[1] if 1 < len(t) else None)),Std.parseInt((t[2] if 2 < len(t) else None)))
        else:
            raise haxe_Exception.thrown(("Invalid date format : " + ("null" if s is None else s)))

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.date = None
        _hx_o.dateUTC = None
Date._hx_class = Date
_hx_classes["Date"] = Date


class EReg:
    _hx_class_name = "EReg"
    __slots__ = ("pattern", "matchObj", "_hx_global")
    _hx_fields = ["pattern", "matchObj", "global"]
    _hx_methods = ["match", "matched", "matchedLeft", "matchedRight", "matchedPos", "matchSub", "split", "replace", "map"]
    _hx_statics = ["escape"]

    def __init__(self,r,opt):
        self.matchObj = None
        self._hx_global = False
        options = 0
        _g = 0
        _g1 = len(opt)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            c = (-1 if ((i >= len(opt))) else ord(opt[i]))
            if (c == 109):
                options = (options | python_lib_Re.M)
            if (c == 105):
                options = (options | python_lib_Re.I)
            if (c == 115):
                options = (options | python_lib_Re.S)
            if (c == 117):
                options = (options | python_lib_Re.U)
            if (c == 103):
                self._hx_global = True
        self.pattern = python_lib_Re.compile(r,options)

    def match(self,s):
        self.matchObj = python_lib_Re.search(self.pattern,s)
        return (self.matchObj is not None)

    def matched(self,n):
        return self.matchObj.group(n)

    def matchedLeft(self):
        return HxString.substr(self.matchObj.string,0,self.matchObj.start())

    def matchedRight(self):
        return HxString.substr(self.matchObj.string,self.matchObj.end(),None)

    def matchedPos(self):
        return _hx_AnonObject({'pos': self.matchObj.start(), 'len': (self.matchObj.end() - self.matchObj.start())})

    def matchSub(self,s,pos,_hx_len = None):
        if (_hx_len is None):
            _hx_len = -1
        if (_hx_len != -1):
            self.matchObj = self.pattern.search(s,pos,(pos + _hx_len))
        else:
            self.matchObj = self.pattern.search(s,pos)
        return (self.matchObj is not None)

    def split(self,s):
        if self._hx_global:
            ret = []
            lastEnd = 0
            x = python_HaxeIterator(python_lib_Re.finditer(self.pattern,s))
            while x.hasNext():
                x1 = x.next()
                x2 = HxString.substring(s,lastEnd,x1.start())
                ret.append(x2)
                lastEnd = x1.end()
            x = HxString.substr(s,lastEnd,None)
            ret.append(x)
            return ret
        else:
            self.matchObj = python_lib_Re.search(self.pattern,s)
            if (self.matchObj is None):
                return [s]
            else:
                return [HxString.substring(s,0,self.matchObj.start()), HxString.substr(s,self.matchObj.end(),None)]

    def replace(self,s,by):
        _this = by.split("$$")
        by = "_hx_#repl#__".join([python_Boot.toString1(x1,'') for x1 in _this])
        def _hx_local_0(x):
            res = by
            g = x.groups()
            _g = 0
            _g1 = len(g)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                gs = g[i]
                if (gs is None):
                    continue
                delimiter = ("$" + HxOverrides.stringOrNull(str((i + 1))))
                _this = (list(res) if ((delimiter == "")) else res.split(delimiter))
                res = gs.join([python_Boot.toString1(x1,'') for x1 in _this])
            _this = res.split("_hx_#repl#__")
            res = "$".join([python_Boot.toString1(x1,'') for x1 in _this])
            return res
        replace = _hx_local_0
        return python_lib_Re.sub(self.pattern,replace,s,(0 if (self._hx_global) else 1))

    def map(self,s,f):
        buf_b = python_lib_io_StringIO()
        pos = 0
        right = s
        cur = self
        while (pos < len(s)):
            if (self.matchObj is None):
                self.matchObj = python_lib_Re.search(self.pattern,s)
            else:
                self.matchObj = self.matchObj.re.search(s,pos)
            if (self.matchObj is None):
                break
            pos1 = self.matchObj.end()
            curPos_pos = cur.matchObj.start()
            curPos_len = (cur.matchObj.end() - cur.matchObj.start())
            buf_b.write(Std.string(HxString.substr(HxString.substr(cur.matchObj.string,0,cur.matchObj.start()),pos,None)))
            buf_b.write(Std.string(f(cur)))
            right = HxString.substr(cur.matchObj.string,cur.matchObj.end(),None)
            if (not self._hx_global):
                buf_b.write(Std.string(right))
                return buf_b.getvalue()
            if (curPos_len == 0):
                buf_b.write(Std.string(("" if (((pos1 < 0) or ((pos1 >= len(s))))) else s[pos1])))
                right = HxString.substr(right,1,None)
                pos = (pos1 + 1)
            else:
                pos = pos1
        buf_b.write(Std.string(right))
        return buf_b.getvalue()

    @staticmethod
    def escape(s):
        return python_lib_Re.escape(s)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.pattern = None
        _hx_o.matchObj = None
        _hx_o._hx_global = None
EReg._hx_class = EReg
_hx_classes["EReg"] = EReg


class _EnumValue_EnumValue_Impl_:
    _hx_class_name = "_EnumValue.EnumValue_Impl_"
    __slots__ = ()
    _hx_statics = ["match"]

    @staticmethod
    def match(this1,pattern):
        return False
_EnumValue_EnumValue_Impl_._hx_class = _EnumValue_EnumValue_Impl_
_hx_classes["_EnumValue.EnumValue_Impl_"] = _EnumValue_EnumValue_Impl_


class IntIterator:
    _hx_class_name = "IntIterator"
    __slots__ = ("min", "max")
    _hx_fields = ["min", "max"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,_hx_min,_hx_max):
        self.min = _hx_min
        self.max = _hx_max

    def hasNext(self):
        return (self.min < self.max)

    def next(self):
        def _hx_local_3():
            def _hx_local_2():
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.min
                _hx_local_0.min = (_hx_local_1 + 1)
                return _hx_local_1
            return _hx_local_2()
        return _hx_local_3()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.min = None
        _hx_o.max = None
IntIterator._hx_class = IntIterator
_hx_classes["IntIterator"] = IntIterator


class Lambda:
    _hx_class_name = "Lambda"
    __slots__ = ()
    _hx_statics = ["array", "list", "map", "mapi", "flatten", "flatMap", "has", "exists", "foreach", "iter", "filter", "fold", "foldi", "count", "empty", "indexOf", "find", "findIndex", "concat"]

    @staticmethod
    def array(it):
        a = list()
        i = HxOverrides.iterator(it)
        while i.hasNext():
            i1 = i.next()
            a.append(i1)
        return a

    @staticmethod
    def list(it):
        l = haxe_ds_List()
        i = HxOverrides.iterator(it)
        while i.hasNext():
            i1 = i.next()
            l.add(i1)
        return l

    @staticmethod
    def map(it,f):
        _g = []
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            x2 = f(x1)
            _g.append(x2)
        return _g

    @staticmethod
    def mapi(it,f):
        i = 0
        _g = []
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            x2 = i
            i = (i + 1)
            x3 = f(x2,x1)
            _g.append(x3)
        return _g

    @staticmethod
    def flatten(it):
        _g = []
        e = HxOverrides.iterator(it)
        while e.hasNext():
            e1 = e.next()
            x = HxOverrides.iterator(e1)
            while x.hasNext():
                x1 = x.next()
                _g.append(x1)
        return _g

    @staticmethod
    def flatMap(it,f):
        _g = []
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            x2 = f(x1)
            _g.append(x2)
        _g1 = []
        e = HxOverrides.iterator(_g)
        while e.hasNext():
            e1 = e.next()
            x = HxOverrides.iterator(e1)
            while x.hasNext():
                x1 = x.next()
                _g1.append(x1)
        return _g1

    @staticmethod
    def has(it,elt):
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            if HxOverrides.eq(x1,elt):
                return True
        return False

    @staticmethod
    def exists(it,f):
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            if f(x1):
                return True
        return False

    @staticmethod
    def foreach(it,f):
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            if (not f(x1)):
                return False
        return True

    @staticmethod
    def iter(it,f):
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            f(x1)

    @staticmethod
    def filter(it,f):
        _g = []
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            if f(x1):
                _g.append(x1)
        return _g

    @staticmethod
    def fold(it,f,first):
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            first = f(x1,first)
        return first

    @staticmethod
    def foldi(it,f,first):
        i = 0
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            first = f(x1,first,i)
            i = (i + 1)
        return first

    @staticmethod
    def count(it,pred = None):
        n = 0
        if (pred is None):
            _ = HxOverrides.iterator(it)
            while _.hasNext():
                _1 = _.next()
                n = (n + 1)
        else:
            x = HxOverrides.iterator(it)
            while x.hasNext():
                x1 = x.next()
                if pred(x1):
                    n = (n + 1)
        return n

    @staticmethod
    def empty(it):
        return (not HxOverrides.iterator(it).hasNext())

    @staticmethod
    def indexOf(it,v):
        i = 0
        v2 = HxOverrides.iterator(it)
        while v2.hasNext():
            v21 = v2.next()
            if HxOverrides.eq(v,v21):
                return i
            i = (i + 1)
        return -1

    @staticmethod
    def find(it,f):
        v = HxOverrides.iterator(it)
        while v.hasNext():
            v1 = v.next()
            if f(v1):
                return v1
        return None

    @staticmethod
    def findIndex(it,f):
        i = 0
        v = HxOverrides.iterator(it)
        while v.hasNext():
            v1 = v.next()
            if f(v1):
                return i
            i = (i + 1)
        return -1

    @staticmethod
    def concat(a,b):
        l = list()
        x = HxOverrides.iterator(a)
        while x.hasNext():
            x1 = x.next()
            l.append(x1)
        x = HxOverrides.iterator(b)
        while x.hasNext():
            x1 = x.next()
            l.append(x1)
        return l
Lambda._hx_class = Lambda
_hx_classes["Lambda"] = Lambda


class Reflect:
    _hx_class_name = "Reflect"
    __slots__ = ()
    _hx_statics = ["hasField", "field", "setField", "getProperty", "setProperty", "callMethod", "fields", "isFunction", "compare", "isClosure", "compareMethods", "isObject", "isEnumValue", "deleteField", "copy", "makeVarArgs"]

    @staticmethod
    def hasField(o,field):
        return python_Boot.hasField(o,field)

    @staticmethod
    def field(o,field):
        return python_Boot.field(o,field)

    @staticmethod
    def setField(o,field,value):
        setattr(o,(("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)),value)

    @staticmethod
    def getProperty(o,field):
        if (o is None):
            return None
        if (field in python_Boot.keywords):
            field = ("_hx_" + field)
        elif ((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95))):
            field = ("_hx_" + field)
        if isinstance(o,_hx_AnonObject):
            return Reflect.field(o,field)
        tmp = Reflect.field(o,("get_" + ("null" if field is None else field)))
        if ((tmp is not None) and callable(tmp)):
            return tmp()
        else:
            return Reflect.field(o,field)

    @staticmethod
    def setProperty(o,field,value):
        field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
        if isinstance(o,_hx_AnonObject):
            setattr(o,field1,value)
        elif hasattr(o,("set_" + ("null" if field1 is None else field1))):
            getattr(o,("set_" + ("null" if field1 is None else field1)))(value)
        else:
            setattr(o,field1,value)

    @staticmethod
    def callMethod(o,func,args):
        if callable(func):
            return func(*args)
        else:
            return None

    @staticmethod
    def fields(o):
        return python_Boot.fields(o)

    @staticmethod
    def isFunction(f):
        if (not ((python_lib_Inspect.isfunction(f) or python_lib_Inspect.ismethod(f)))):
            return python_Boot.hasField(f,"func_code")
        else:
            return True

    @staticmethod
    def compare(a,b):
        if ((a is None) and ((b is None))):
            return 0
        if (a is None):
            return 1
        elif (b is None):
            return -1
        elif HxOverrides.eq(a,b):
            return 0
        elif (a > b):
            return 1
        else:
            return -1

    @staticmethod
    def isClosure(v):
        return isinstance(v,python_internal_MethodClosure)

    @staticmethod
    def compareMethods(f1,f2):
        if HxOverrides.eq(f1,f2):
            return True
        if (isinstance(f1,python_internal_MethodClosure) and isinstance(f2,python_internal_MethodClosure)):
            m1 = f1
            m2 = f2
            if HxOverrides.eq(m1.obj,m2.obj):
                return (m1.func == m2.func)
            else:
                return False
        if ((not Reflect.isFunction(f1)) or (not Reflect.isFunction(f2))):
            return False
        return False

    @staticmethod
    def isObject(v):
        _g = Type.typeof(v)
        tmp = _g.index
        if (tmp == 4):
            return True
        elif (tmp == 6):
            _g1 = _g.params[0]
            return True
        else:
            return False

    @staticmethod
    def isEnumValue(v):
        if not HxOverrides.eq(v,Enum):
            return isinstance(v,Enum)
        else:
            return False

    @staticmethod
    def deleteField(o,field):
        if (field in python_Boot.keywords):
            field = ("_hx_" + field)
        elif ((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95))):
            field = ("_hx_" + field)
        if (not python_Boot.hasField(o,field)):
            return False
        o.__delattr__(field)
        return True

    @staticmethod
    def copy(o):
        if (o is None):
            return None
        o2 = _hx_AnonObject({})
        _g = 0
        _g1 = python_Boot.fields(o)
        while (_g < len(_g1)):
            f = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            value = Reflect.field(o,f)
            setattr(o2,(("_hx_" + f) if ((f in python_Boot.keywords)) else (("_hx_" + f) if (((((len(f) > 2) and ((ord(f[0]) == 95))) and ((ord(f[1]) == 95))) and ((ord(f[(len(f) - 1)]) != 95)))) else f)),value)
        return o2

    @staticmethod
    def makeVarArgs(f):
        def _hx_local_0(*v):
            this1 = v
            return f((list(this1) if ((not Std.isOfType(this1,list))) else this1))
        return _hx_local_0
Reflect._hx_class = Reflect
_hx_classes["Reflect"] = Reflect


class Std:
    _hx_class_name = "Std"
    __slots__ = ()
    _hx_statics = ["downcast", "instance", "isMetaType", "is", "isOfType", "string", "int", "parseInt", "shortenPossibleNumber", "parseFloat", "random"]

    @staticmethod
    def downcast(value,c):
        try:
            tmp = None
            if (not isinstance(value,c)):
                if c._hx_is_interface:
                    cls = c
                    loop = None
                    def _hx_local_1(intf):
                        f = (intf._hx_interfaces if (hasattr(intf,"_hx_interfaces")) else [])
                        if (f is not None):
                            _g = 0
                            while (_g < len(f)):
                                i = (f[_g] if _g >= 0 and _g < len(f) else None)
                                _g = (_g + 1)
                                if (i == cls):
                                    return True
                                else:
                                    l = loop(i)
                                    if l:
                                        return True
                            return False
                        else:
                            return False
                    loop = _hx_local_1
                    currentClass = value.__class__
                    result = False
                    while (currentClass is not None):
                        if loop(currentClass):
                            result = True
                            break
                        currentClass = python_Boot.getSuperClass(currentClass)
                    tmp = result
                else:
                    tmp = False
            else:
                tmp = True
            if tmp:
                return value
            else:
                return None
        except BaseException as _g:
            None
            return None

    @staticmethod
    def instance(value,c):
        return Std.downcast(value,c)

    @staticmethod
    def isMetaType(v,t):
        return ((type(v) == type) and (v == t))

    @staticmethod
    def _hx_is(v,t):
        return Std.isOfType(v,t)

    @staticmethod
    def isOfType(v,t):
        if ((v is None) and ((t is None))):
            return False
        if (t is None):
            return False
        if ((type(t) == type) and (t == Dynamic)):
            return (v is not None)
        isBool = isinstance(v,bool)
        if (((type(t) == type) and (t == Bool)) and isBool):
            return True
        if ((((not isBool) and (not ((type(t) == type) and (t == Bool)))) and ((type(t) == type) and (t == Int))) and isinstance(v,int)):
            return True
        vIsFloat = isinstance(v,float)
        tmp = None
        tmp1 = None
        if (((not isBool) and vIsFloat) and ((type(t) == type) and (t == Int))):
            f = v
            tmp1 = (((f != Math.POSITIVE_INFINITY) and ((f != Math.NEGATIVE_INFINITY))) and (not python_lib_Math.isnan(f)))
        else:
            tmp1 = False
        if tmp1:
            tmp1 = None
            try:
                tmp1 = int(v)
            except BaseException as _g:
                None
                tmp1 = None
            tmp = (v == tmp1)
        else:
            tmp = False
        if ((tmp and ((v <= 2147483647))) and ((v >= -2147483648))):
            return True
        if (((not isBool) and ((type(t) == type) and (t == Float))) and isinstance(v,(float, int))):
            return True
        if ((type(t) == type) and (t == str)):
            return isinstance(v,str)
        isEnumType = ((type(t) == type) and (t == Enum))
        if ((isEnumType and python_lib_Inspect.isclass(v)) and hasattr(v,"_hx_constructs")):
            return True
        if isEnumType:
            return False
        isClassType = ((type(t) == type) and (t == Class))
        if ((((isClassType and (not isinstance(v,Enum))) and python_lib_Inspect.isclass(v)) and hasattr(v,"_hx_class_name")) and (not hasattr(v,"_hx_constructs"))):
            return True
        if isClassType:
            return False
        tmp = None
        try:
            tmp = isinstance(v,t)
        except BaseException as _g:
            None
            tmp = False
        if tmp:
            return True
        if python_lib_Inspect.isclass(t):
            cls = t
            loop = None
            def _hx_local_1(intf):
                f = (intf._hx_interfaces if (hasattr(intf,"_hx_interfaces")) else [])
                if (f is not None):
                    _g = 0
                    while (_g < len(f)):
                        i = (f[_g] if _g >= 0 and _g < len(f) else None)
                        _g = (_g + 1)
                        if (i == cls):
                            return True
                        else:
                            l = loop(i)
                            if l:
                                return True
                    return False
                else:
                    return False
            loop = _hx_local_1
            currentClass = v.__class__
            result = False
            while (currentClass is not None):
                if loop(currentClass):
                    result = True
                    break
                currentClass = python_Boot.getSuperClass(currentClass)
            return result
        else:
            return False

    @staticmethod
    def string(s):
        return python_Boot.toString1(s,"")

    @staticmethod
    def int(x):
        try:
            return int(x)
        except BaseException as _g:
            None
            return None

    @staticmethod
    def parseInt(x):
        if (x is None):
            return None
        try:
            return int(x)
        except BaseException as _g:
            None
            base = 10
            _hx_len = len(x)
            foundCount = 0
            sign = 0
            firstDigitIndex = 0
            lastDigitIndex = -1
            previous = 0
            _g = 0
            _g1 = _hx_len
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                c = (-1 if ((i >= len(x))) else ord(x[i]))
                if (((c > 8) and ((c < 14))) or ((c == 32))):
                    if (foundCount > 0):
                        return None
                    continue
                else:
                    c1 = c
                    if (c1 == 43):
                        if (foundCount == 0):
                            sign = 1
                        elif (not (((48 <= c) and ((c <= 57))))):
                            if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                break
                    elif (c1 == 45):
                        if (foundCount == 0):
                            sign = -1
                        elif (not (((48 <= c) and ((c <= 57))))):
                            if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                break
                    elif (c1 == 48):
                        if (not (((foundCount == 0) or (((foundCount == 1) and ((sign != 0))))))):
                            if (not (((48 <= c) and ((c <= 57))))):
                                if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                    break
                    elif ((c1 == 120) or ((c1 == 88))):
                        if ((previous == 48) and ((((foundCount == 1) and ((sign == 0))) or (((foundCount == 2) and ((sign != 0))))))):
                            base = 16
                        elif (not (((48 <= c) and ((c <= 57))))):
                            if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                break
                    elif (not (((48 <= c) and ((c <= 57))))):
                        if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                            break
                if (((foundCount == 0) and ((sign == 0))) or (((foundCount == 1) and ((sign != 0))))):
                    firstDigitIndex = i
                foundCount = (foundCount + 1)
                lastDigitIndex = i
                previous = c
            if (firstDigitIndex <= lastDigitIndex):
                digits = HxString.substring(x,firstDigitIndex,(lastDigitIndex + 1))
                try:
                    return (((-1 if ((sign == -1)) else 1)) * int(digits,base))
                except BaseException as _g:
                    return None
            return None

    @staticmethod
    def shortenPossibleNumber(x):
        r = ""
        _g = 0
        _g1 = len(x)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            c = ("" if (((i < 0) or ((i >= len(x))))) else x[i])
            _g2 = HxString.charCodeAt(c,0)
            if (_g2 is None):
                break
            else:
                _g3 = _g2
                if (((((((((((_g3 == 57) or ((_g3 == 56))) or ((_g3 == 55))) or ((_g3 == 54))) or ((_g3 == 53))) or ((_g3 == 52))) or ((_g3 == 51))) or ((_g3 == 50))) or ((_g3 == 49))) or ((_g3 == 48))) or ((_g3 == 46))):
                    r = (("null" if r is None else r) + ("null" if c is None else c))
                else:
                    break
        return r

    @staticmethod
    def parseFloat(x):
        try:
            return float(x)
        except BaseException as _g:
            None
            if (x is not None):
                r1 = Std.shortenPossibleNumber(x)
                if (r1 != x):
                    return Std.parseFloat(r1)
            return Math.NaN

    @staticmethod
    def random(x):
        if (x <= 0):
            return 0
        else:
            return int((python_lib_Random.random() * x))
Std._hx_class = Std
_hx_classes["Std"] = Std


class Float: pass


class Int: pass


class Bool: pass


class Dynamic: pass


class StringBuf:
    _hx_class_name = "StringBuf"
    __slots__ = ("b",)
    _hx_fields = ["b"]
    _hx_methods = ["get_length", "add", "add1", "addChar", "addSub", "toString"]

    def __init__(self):
        self.b = python_lib_io_StringIO()

    def get_length(self):
        pos = self.b.tell()
        self.b.seek(0,2)
        _hx_len = self.b.tell()
        self.b.seek(pos,0)
        return _hx_len

    def add(self,x):
        s = Std.string(x)
        self.b.write(s)

    def add1(self,s):
        self.b.write(s)

    def addChar(self,c):
        s = "".join(map(chr,[c]))
        self.b.write(s)

    def addSub(self,s,pos,_hx_len = None):
        s1 = (HxString.substr(s,pos,None) if ((_hx_len is None)) else HxString.substr(s,pos,_hx_len))
        self.b.write(s1)

    def toString(self):
        return self.b.getvalue()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.b = None
StringBuf._hx_class = StringBuf
_hx_classes["StringBuf"] = StringBuf


class haxe_SysTools:
    _hx_class_name = "haxe.SysTools"
    __slots__ = ()
    _hx_statics = ["winMetaCharacters", "quoteUnixArg", "quoteWinArg"]

    @staticmethod
    def quoteUnixArg(argument):
        if (argument == ""):
            return "''"
        _this = EReg("[^a-zA-Z0-9_@%+=:,./-]","")
        _this.matchObj = python_lib_Re.search(_this.pattern,argument)
        if (_this.matchObj is None):
            return argument
        return (("'" + HxOverrides.stringOrNull(StringTools.replace(argument,"'","'\"'\"'"))) + "'")

    @staticmethod
    def quoteWinArg(argument,escapeMetaCharacters):
        _this = EReg("^[^ \t\\\\\"]+$","")
        _this.matchObj = python_lib_Re.search(_this.pattern,argument)
        if (_this.matchObj is None):
            result_b = python_lib_io_StringIO()
            needquote = None
            startIndex = None
            if (((argument.find(" ") if ((startIndex is None)) else HxString.indexOfImpl(argument," ",startIndex))) == -1):
                startIndex = None
                needquote = (((argument.find("\t") if ((startIndex is None)) else HxString.indexOfImpl(argument,"\t",startIndex))) != -1)
            else:
                needquote = True
            needquote1 = (needquote or ((argument == "")))
            if needquote1:
                result_b.write("\"")
            bs_buf = StringBuf()
            _g = 0
            _g1 = len(argument)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                _g2 = HxString.charCodeAt(argument,i)
                if (_g2 is None):
                    c = _g2
                    if (bs_buf.get_length() > 0):
                        result_b.write(Std.string(bs_buf.b.getvalue()))
                        bs_buf = StringBuf()
                    result_b.write("".join(map(chr,[c])))
                else:
                    _g3 = _g2
                    if (_g3 == 34):
                        bs = bs_buf.b.getvalue()
                        result_b.write(Std.string(bs))
                        result_b.write(Std.string(bs))
                        bs_buf = StringBuf()
                        result_b.write("\\\"")
                    elif (_g3 == 92):
                        bs_buf.b.write("\\")
                    else:
                        c1 = _g2
                        if (bs_buf.get_length() > 0):
                            result_b.write(Std.string(bs_buf.b.getvalue()))
                            bs_buf = StringBuf()
                        result_b.write("".join(map(chr,[c1])))
            result_b.write(Std.string(bs_buf.b.getvalue()))
            if needquote1:
                result_b.write(Std.string(bs_buf.b.getvalue()))
                result_b.write("\"")
            argument = result_b.getvalue()
        if escapeMetaCharacters:
            result_b = python_lib_io_StringIO()
            _g = 0
            _g1 = len(argument)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                c = HxString.charCodeAt(argument,i)
                if (python_internal_ArrayImpl.indexOf(haxe_SysTools.winMetaCharacters,c,None) >= 0):
                    result_b.write("".join(map(chr,[94])))
                result_b.write("".join(map(chr,[c])))
            return result_b.getvalue()
        else:
            return argument
haxe_SysTools._hx_class = haxe_SysTools
_hx_classes["haxe.SysTools"] = haxe_SysTools


class StringTools:
    _hx_class_name = "StringTools"
    __slots__ = ()
    _hx_statics = ["urlEncode", "urlDecode", "htmlEscape", "htmlUnescape", "contains", "startsWith", "endsWith", "isSpace", "ltrim", "rtrim", "trim", "lpad", "rpad", "replace", "hex", "fastCodeAt", "unsafeCodeAt", "iterator", "keyValueIterator", "isEof", "quoteUnixArg", "winMetaCharacters", "quoteWinArg"]

    @staticmethod
    def urlEncode(s):
        return python_lib_urllib_Parse.quote(s,"")

    @staticmethod
    def urlDecode(s):
        return python_lib_urllib_Parse.unquote(s)

    @staticmethod
    def htmlEscape(s,quotes = None):
        buf_b = python_lib_io_StringIO()
        _g_offset = 0
        _g_s = s
        while (_g_offset < len(_g_s)):
            index = _g_offset
            _g_offset = (_g_offset + 1)
            code = ord(_g_s[index])
            code1 = code
            if (code1 == 34):
                if quotes:
                    buf_b.write("&quot;")
                else:
                    buf_b.write("".join(map(chr,[code])))
            elif (code1 == 38):
                buf_b.write("&amp;")
            elif (code1 == 39):
                if quotes:
                    buf_b.write("&#039;")
                else:
                    buf_b.write("".join(map(chr,[code])))
            elif (code1 == 60):
                buf_b.write("&lt;")
            elif (code1 == 62):
                buf_b.write("&gt;")
            else:
                buf_b.write("".join(map(chr,[code])))
        return buf_b.getvalue()

    @staticmethod
    def htmlUnescape(s):
        _this = s.split("&gt;")
        _this1 = ">".join([python_Boot.toString1(x1,'') for x1 in _this])
        _this = _this1.split("&lt;")
        _this1 = "<".join([python_Boot.toString1(x1,'') for x1 in _this])
        _this = _this1.split("&quot;")
        _this1 = "\"".join([python_Boot.toString1(x1,'') for x1 in _this])
        _this = _this1.split("&#039;")
        _this1 = "'".join([python_Boot.toString1(x1,'') for x1 in _this])
        _this = _this1.split("&amp;")
        return "&".join([python_Boot.toString1(x1,'') for x1 in _this])

    @staticmethod
    def contains(s,value):
        startIndex = None
        return (((s.find(value) if ((startIndex is None)) else HxString.indexOfImpl(s,value,startIndex))) != -1)

    @staticmethod
    def startsWith(s,start):
        return s.startswith(start)

    @staticmethod
    def endsWith(s,end):
        return s.endswith(end)

    @staticmethod
    def isSpace(s,pos):
        if (((len(s) == 0) or ((pos < 0))) or ((pos >= len(s)))):
            return False
        c = HxString.charCodeAt(s,pos)
        if (not (((c > 8) and ((c < 14))))):
            return (c == 32)
        else:
            return True

    @staticmethod
    def ltrim(s):
        l = len(s)
        r = 0
        while ((r < l) and StringTools.isSpace(s,r)):
            r = (r + 1)
        if (r > 0):
            return HxString.substr(s,r,(l - r))
        else:
            return s

    @staticmethod
    def rtrim(s):
        l = len(s)
        r = 0
        while ((r < l) and StringTools.isSpace(s,((l - r) - 1))):
            r = (r + 1)
        if (r > 0):
            return HxString.substr(s,0,(l - r))
        else:
            return s

    @staticmethod
    def trim(s):
        return StringTools.ltrim(StringTools.rtrim(s))

    @staticmethod
    def lpad(s,c,l):
        if (len(c) <= 0):
            return s
        buf = StringBuf()
        l = (l - len(s))
        while (buf.get_length() < l):
            s1 = Std.string(c)
            buf.b.write(s1)
        s1 = Std.string(s)
        buf.b.write(s1)
        return buf.b.getvalue()

    @staticmethod
    def rpad(s,c,l):
        if (len(c) <= 0):
            return s
        buf = StringBuf()
        s1 = Std.string(s)
        buf.b.write(s1)
        while (buf.get_length() < l):
            s = Std.string(c)
            buf.b.write(s)
        return buf.b.getvalue()

    @staticmethod
    def replace(s,sub,by):
        _this = (list(s) if ((sub == "")) else s.split(sub))
        return by.join([python_Boot.toString1(x1,'') for x1 in _this])

    @staticmethod
    def hex(n,digits = None):
        s = ""
        hexChars = "0123456789ABCDEF"
        while True:
            index = (n & 15)
            s = (HxOverrides.stringOrNull((("" if (((index < 0) or ((index >= len(hexChars))))) else hexChars[index]))) + ("null" if s is None else s))
            n = HxOverrides.rshift(n, 4)
            if (not ((n > 0))):
                break
        if ((digits is not None) and ((len(s) < digits))):
            diff = (digits - len(s))
            _g = 0
            _g1 = diff
            while (_g < _g1):
                _ = _g
                _g = (_g + 1)
                s = ("0" + ("null" if s is None else s))
        return s

    @staticmethod
    def fastCodeAt(s,index):
        if (index >= len(s)):
            return -1
        else:
            return ord(s[index])

    @staticmethod
    def unsafeCodeAt(s,index):
        return ord(s[index])

    @staticmethod
    def iterator(s):
        return haxe_iterators_StringIterator(s)

    @staticmethod
    def keyValueIterator(s):
        return haxe_iterators_StringKeyValueIterator(s)

    @staticmethod
    def isEof(c):
        return (c == -1)

    @staticmethod
    def quoteUnixArg(argument):
        if (argument == ""):
            return "''"
        else:
            _this = EReg("[^a-zA-Z0-9_@%+=:,./-]","")
            _this.matchObj = python_lib_Re.search(_this.pattern,argument)
            if (_this.matchObj is None):
                return argument
            else:
                return (("'" + HxOverrides.stringOrNull(StringTools.replace(argument,"'","'\"'\"'"))) + "'")

    @staticmethod
    def quoteWinArg(argument,escapeMetaCharacters):
        argument1 = argument
        _this = EReg("^[^ \t\\\\\"]+$","")
        _this.matchObj = python_lib_Re.search(_this.pattern,argument1)
        if (_this.matchObj is None):
            result_b = python_lib_io_StringIO()
            needquote = None
            startIndex = None
            if (((argument1.find(" ") if ((startIndex is None)) else HxString.indexOfImpl(argument1," ",startIndex))) == -1):
                startIndex = None
                needquote = (((argument1.find("\t") if ((startIndex is None)) else HxString.indexOfImpl(argument1,"\t",startIndex))) != -1)
            else:
                needquote = True
            needquote1 = (needquote or ((argument1 == "")))
            if needquote1:
                result_b.write("\"")
            bs_buf = StringBuf()
            _g = 0
            _g1 = len(argument1)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                _g2 = HxString.charCodeAt(argument1,i)
                if (_g2 is None):
                    c = _g2
                    if (bs_buf.get_length() > 0):
                        result_b.write(Std.string(bs_buf.b.getvalue()))
                        bs_buf = StringBuf()
                    result_b.write("".join(map(chr,[c])))
                else:
                    _g3 = _g2
                    if (_g3 == 34):
                        bs = bs_buf.b.getvalue()
                        result_b.write(Std.string(bs))
                        result_b.write(Std.string(bs))
                        bs_buf = StringBuf()
                        result_b.write("\\\"")
                    elif (_g3 == 92):
                        bs_buf.b.write("\\")
                    else:
                        c1 = _g2
                        if (bs_buf.get_length() > 0):
                            result_b.write(Std.string(bs_buf.b.getvalue()))
                            bs_buf = StringBuf()
                        result_b.write("".join(map(chr,[c1])))
            result_b.write(Std.string(bs_buf.b.getvalue()))
            if needquote1:
                result_b.write(Std.string(bs_buf.b.getvalue()))
                result_b.write("\"")
            argument1 = result_b.getvalue()
        if escapeMetaCharacters:
            result_b = python_lib_io_StringIO()
            _g = 0
            _g1 = len(argument1)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                c = HxString.charCodeAt(argument1,i)
                if (python_internal_ArrayImpl.indexOf(haxe_SysTools.winMetaCharacters,c,None) >= 0):
                    result_b.write("".join(map(chr,[94])))
                result_b.write("".join(map(chr,[c])))
            return result_b.getvalue()
        else:
            return argument1
StringTools._hx_class = StringTools
_hx_classes["StringTools"] = StringTools


class sys_FileSystem:
    _hx_class_name = "sys.FileSystem"
    __slots__ = ()
    _hx_statics = ["exists", "stat", "rename", "fullPath", "absolutePath", "isDirectory", "createDirectory", "deleteFile", "deleteDirectory", "readDirectory"]

    @staticmethod
    def exists(path):
        return python_lib_os_Path.exists(path)

    @staticmethod
    def stat(path):
        s = python_lib_Os.stat(path)
        return _hx_AnonObject({'gid': s.st_gid, 'uid': s.st_uid, 'atime': Date.fromTime((1000 * s.st_atime)), 'mtime': Date.fromTime((1000 * s.st_mtime)), 'ctime': Date.fromTime((1000 * s.st_ctime)), 'size': s.st_size, 'dev': s.st_dev, 'ino': s.st_ino, 'nlink': s.st_nlink, 'rdev': getattr(s,"st_rdev",0), 'mode': s.st_mode})

    @staticmethod
    def rename(path,newPath):
        python_lib_Os.rename(path,newPath)

    @staticmethod
    def fullPath(relPath):
        return python_lib_os_Path.realpath(relPath)

    @staticmethod
    def absolutePath(relPath):
        if haxe_io_Path.isAbsolute(relPath):
            return relPath
        return haxe_io_Path.join([Sys.getCwd(), relPath])

    @staticmethod
    def isDirectory(path):
        return python_lib_os_Path.isdir(path)

    @staticmethod
    def createDirectory(path):
        python_lib_Os.makedirs(path,511,True)

    @staticmethod
    def deleteFile(path):
        python_lib_Os.remove(path)

    @staticmethod
    def deleteDirectory(path):
        python_lib_Os.rmdir(path)

    @staticmethod
    def readDirectory(path):
        return python_lib_Os.listdir(path)
sys_FileSystem._hx_class = sys_FileSystem
_hx_classes["sys.FileSystem"] = sys_FileSystem


class Sys:
    _hx_class_name = "Sys"
    __slots__ = ()
    _hx_statics = ["environ", "get_environ", "time", "exit", "print", "println", "args", "getEnv", "putEnv", "environment", "sleep", "setTimeLocale", "getCwd", "setCwd", "systemName", "command", "cpuTime", "executablePath", "_programPath", "programPath", "getChar", "stdin", "stdout", "stderr"]
    environ = None

    @staticmethod
    def get_environ():
        _g = Sys.environ
        if (_g is None):
            environ = haxe_ds_StringMap()
            env = python_lib_Os.environ
            key = python_HaxeIterator(iter(env.keys()))
            while key.hasNext():
                key1 = key.next()
                value = env.get(key1,None)
                environ.h[key1] = value
            def _hx_local_1():
                def _hx_local_0():
                    Sys.environ = environ
                    return Sys.environ
                return _hx_local_0()
            return _hx_local_1()
        else:
            env = _g
            return env

    @staticmethod
    def time():
        return python_lib_Time.time()

    @staticmethod
    def exit(code):
        python_lib_Sys.exit(code)

    @staticmethod
    def print(v):
        python_Lib.printString(Std.string(v))

    @staticmethod
    def println(v):
        _hx_str = Std.string(v)
        python_Lib.printString((("" + ("null" if _hx_str is None else _hx_str)) + HxOverrides.stringOrNull(python_Lib.lineEnd)))

    @staticmethod
    def args():
        argv = python_lib_Sys.argv
        return argv[1:None]

    @staticmethod
    def getEnv(s):
        return Sys.get_environ().h.get(s,None)

    @staticmethod
    def putEnv(s,v):
        python_lib_Os.putenv(s,v)
        Sys.get_environ().h[s] = v

    @staticmethod
    def environment():
        return Sys.get_environ()

    @staticmethod
    def sleep(seconds):
        python_lib_Time.sleep(seconds)

    @staticmethod
    def setTimeLocale(loc):
        return False

    @staticmethod
    def getCwd():
        return python_lib_Os.getcwd()

    @staticmethod
    def setCwd(s):
        python_lib_Os.chdir(s)

    @staticmethod
    def systemName():
        _g = python_lib_Sys.platform
        x = _g
        if x.startswith("linux"):
            return "Linux"
        else:
            _g1 = _g
            _hx_local_0 = len(_g1)
            if (_hx_local_0 == 5):
                if (_g1 == "win32"):
                    return "Windows"
                else:
                    raise haxe_Exception.thrown("not supported platform")
            elif (_hx_local_0 == 6):
                if (_g1 == "cygwin"):
                    return "Windows"
                elif (_g1 == "darwin"):
                    return "Mac"
                else:
                    raise haxe_Exception.thrown("not supported platform")
            else:
                raise haxe_Exception.thrown("not supported platform")

    @staticmethod
    def command(cmd,args = None):
        if (args is None):
            return python_lib_Subprocess.call(cmd,**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'shell': True})))
        else:
            return python_lib_Subprocess.call(([cmd] + args))

    @staticmethod
    def cpuTime():
        return python_lib_Timeit.default_timer()

    @staticmethod
    def executablePath():
        return python_internal_ArrayImpl._get(python_lib_Sys.argv, 0)

    @staticmethod
    def programPath():
        return Sys._programPath

    @staticmethod
    def getChar(echo):
        ch = None
        _g = Sys.systemName()
        _g1 = _g
        _hx_local_0 = len(_g1)
        if (_hx_local_0 == 5):
            if (_g1 == "Linux"):
                fd = python_lib_Sys.stdin.fileno()
                old = python_lib_Termios.tcgetattr(fd)
                fileNo = fd
                when = python_lib_Termios.TCSADRAIN
                settings = old
                def _hx_local_1():
                    python_lib_Termios.tcsetattr(fileNo,when,settings)
                restore = _hx_local_1
                try:
                    python_lib_Tty.setraw(fd)
                    x = python_lib_Sys.stdin.read(1)
                    restore()
                    ch = HxString.charCodeAt(x,0)
                except BaseException as _g1:
                    None
                    e = haxe_Exception.caught(_g1).unwrap()
                    restore()
                    raise haxe_Exception.thrown(e)
            else:
                x = _g
                raise haxe_Exception.thrown((("platform " + ("null" if x is None else x)) + " not supported"))
        elif (_hx_local_0 == 3):
            if (_g1 == "Mac"):
                fd = python_lib_Sys.stdin.fileno()
                old = python_lib_Termios.tcgetattr(fd)
                fileNo = fd
                when = python_lib_Termios.TCSADRAIN
                settings = old
                def _hx_local_2():
                    python_lib_Termios.tcsetattr(fileNo,when,settings)
                restore = _hx_local_2
                try:
                    python_lib_Tty.setraw(fd)
                    x = python_lib_Sys.stdin.read(1)
                    restore()
                    ch = HxString.charCodeAt(x,0)
                except BaseException as _g1:
                    None
                    e = haxe_Exception.caught(_g1).unwrap()
                    restore()
                    raise haxe_Exception.thrown(e)
            else:
                x = _g
                raise haxe_Exception.thrown((("platform " + ("null" if x is None else x)) + " not supported"))
        elif (_hx_local_0 == 7):
            if (_g1 == "Windows"):
                ch = HxString.charCodeAt(python_lib_Msvcrt.getwch(),0)
            else:
                x = _g
                raise haxe_Exception.thrown((("platform " + ("null" if x is None else x)) + " not supported"))
        else:
            x = _g
            raise haxe_Exception.thrown((("platform " + ("null" if x is None else x)) + " not supported"))
        if echo:
            python_Lib.printString(Std.string("".join(map(chr,[ch]))))
        return ch

    @staticmethod
    def stdin():
        return python_io_IoTools.createFileInputFromText(python_lib_Sys.stdin)

    @staticmethod
    def stdout():
        return python_io_IoTools.createFileOutputFromText(python_lib_Sys.stdout)

    @staticmethod
    def stderr():
        return python_io_IoTools.createFileOutputFromText(python_lib_Sys.stderr)
Sys._hx_class = Sys
_hx_classes["Sys"] = Sys

class ValueType(Enum):
    __slots__ = ()
    _hx_class_name = "ValueType"
    _hx_constructs = ["TNull", "TInt", "TFloat", "TBool", "TObject", "TFunction", "TClass", "TEnum", "TUnknown"]

    @staticmethod
    def TClass(c):
        return ValueType("TClass", 6, (c,))

    @staticmethod
    def TEnum(e):
        return ValueType("TEnum", 7, (e,))
ValueType.TNull = ValueType("TNull", 0, ())
ValueType.TInt = ValueType("TInt", 1, ())
ValueType.TFloat = ValueType("TFloat", 2, ())
ValueType.TBool = ValueType("TBool", 3, ())
ValueType.TObject = ValueType("TObject", 4, ())
ValueType.TFunction = ValueType("TFunction", 5, ())
ValueType.TUnknown = ValueType("TUnknown", 8, ())
ValueType._hx_class = ValueType
_hx_classes["ValueType"] = ValueType


class Type:
    _hx_class_name = "Type"
    __slots__ = ()
    _hx_statics = ["getClass", "getEnum", "getSuperClass", "getClassName", "getEnumName", "resolveClass", "resolveEnum", "createInstance", "createEmptyInstance", "createEnum", "createEnumIndex", "getInstanceFields", "getClassFields", "getEnumConstructs", "typeof", "asEnumImpl", "enumEq", "enumConstructor", "enumParameters", "enumIndex", "allEnums"]

    @staticmethod
    def getClass(o):
        if (o is None):
            return None
        o1 = o
        if ((o1 is not None) and ((HxOverrides.eq(o1,str) or python_lib_Inspect.isclass(o1)))):
            return None
        if isinstance(o,_hx_AnonObject):
            return None
        if hasattr(o,"_hx_class"):
            return o._hx_class
        if hasattr(o,"__class__"):
            return o.__class__
        else:
            return None

    @staticmethod
    def getEnum(o):
        if (o is None):
            return None
        return o.__class__

    @staticmethod
    def getSuperClass(c):
        return python_Boot.getSuperClass(c)

    @staticmethod
    def getClassName(c):
        if hasattr(c,"_hx_class_name"):
            return c._hx_class_name
        else:
            if (c == list):
                return "Array"
            if (c == Math):
                return "Math"
            if (c == str):
                return "String"
            try:
                return c.__name__
            except BaseException as _g:
                None
                return None

    @staticmethod
    def getEnumName(e):
        return e._hx_class_name

    @staticmethod
    def resolveClass(name):
        if (name == "Array"):
            return list
        if (name == "Math"):
            return Math
        if (name == "String"):
            return str
        cl = _hx_classes.get(name,None)
        tmp = None
        if (cl is not None):
            o = cl
            tmp = (not (((o is not None) and ((HxOverrides.eq(o,str) or python_lib_Inspect.isclass(o))))))
        else:
            tmp = True
        if tmp:
            return None
        return cl

    @staticmethod
    def resolveEnum(name):
        if (name == "Bool"):
            return Bool
        o = Type.resolveClass(name)
        if hasattr(o,"_hx_constructs"):
            return o
        else:
            return None

    @staticmethod
    def createInstance(cl,args):
        return cl(*args)

    @staticmethod
    def createEmptyInstance(cl):
        i = cl.__new__(cl)
        callInit = None
        def _hx_local_0(cl):
            sc = Type.getSuperClass(cl)
            if (sc is not None):
                callInit(sc)
            if hasattr(cl,"_hx_empty_init"):
                cl._hx_empty_init(i)
        callInit = _hx_local_0
        callInit(cl)
        return i

    @staticmethod
    def createEnum(e,constr,params = None):
        f = Reflect.field(e,constr)
        if (f is None):
            raise haxe_Exception.thrown(("No such constructor " + ("null" if constr is None else constr)))
        if Reflect.isFunction(f):
            if (params is None):
                raise haxe_Exception.thrown((("Constructor " + ("null" if constr is None else constr)) + " need parameters"))
            return Reflect.callMethod(e,f,params)
        if ((params is not None) and ((len(params) != 0))):
            raise haxe_Exception.thrown((("Constructor " + ("null" if constr is None else constr)) + " does not need parameters"))
        return f

    @staticmethod
    def createEnumIndex(e,index,params = None):
        c = python_internal_ArrayImpl._get(e._hx_constructs, index)
        if (c is None):
            raise haxe_Exception.thrown((Std.string(index) + " is not a valid enum constructor index"))
        return Type.createEnum(e,c,params)

    @staticmethod
    def getInstanceFields(c):
        return python_Boot.getInstanceFields(c)

    @staticmethod
    def getClassFields(c):
        return python_Boot.getClassFields(c)

    @staticmethod
    def getEnumConstructs(e):
        if hasattr(e,"_hx_constructs"):
            x = e._hx_constructs
            return list(x)
        else:
            return []

    @staticmethod
    def typeof(v):
        if (v is None):
            return ValueType.TNull
        elif isinstance(v,bool):
            return ValueType.TBool
        elif isinstance(v,int):
            return ValueType.TInt
        elif isinstance(v,float):
            return ValueType.TFloat
        elif isinstance(v,str):
            return ValueType.TClass(str)
        elif isinstance(v,list):
            return ValueType.TClass(list)
        elif (isinstance(v,_hx_AnonObject) or python_lib_Inspect.isclass(v)):
            return ValueType.TObject
        elif isinstance(v,Enum):
            return ValueType.TEnum(v.__class__)
        elif (isinstance(v,type) or hasattr(v,"_hx_class")):
            return ValueType.TClass(v.__class__)
        elif callable(v):
            return ValueType.TFunction
        else:
            return ValueType.TUnknown

    @staticmethod
    def asEnumImpl(x):
        return x

    @staticmethod
    def enumEq(a,b):
        if HxOverrides.eq(a,b):
            return True
        try:
            if ((b is None) and (not HxOverrides.eq(a,b))):
                return False
            if (a.tag != b.tag):
                return False
            p1 = a.params
            p2 = b.params
            if (len(p1) != len(p2)):
                return False
            _g = 0
            _g1 = len(p1)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                if (not Type.enumEq(p1[i],p2[i])):
                    return False
            if (a._hx_class != b._hx_class):
                return False
        except BaseException as _g:
            None
            return False
        return True

    @staticmethod
    def enumConstructor(e):
        return e.tag

    @staticmethod
    def enumParameters(e):
        return list(e.params)

    @staticmethod
    def enumIndex(e):
        return e.index

    @staticmethod
    def allEnums(e):
        ctors = Type.getEnumConstructs(e)
        ret = []
        _g = 0
        while (_g < len(ctors)):
            ctor = (ctors[_g] if _g >= 0 and _g < len(ctors) else None)
            _g = (_g + 1)
            v = Reflect.field(e,ctor)
            if Std.isOfType(v,e):
                ret.append(v)
        return ret
Type._hx_class = Type
_hx_classes["Type"] = Type


class _Xml_XmlType_Impl_:
    _hx_class_name = "_Xml.XmlType_Impl_"
    __slots__ = ()
    _hx_statics = ["Element", "PCData", "CData", "Comment", "DocType", "ProcessingInstruction", "Document", "toString"]

    @staticmethod
    def toString(this1):
        _g = this1
        if (_g == 0):
            return "Element"
        elif (_g == 1):
            return "PCData"
        elif (_g == 2):
            return "CData"
        elif (_g == 3):
            return "Comment"
        elif (_g == 4):
            return "DocType"
        elif (_g == 5):
            return "ProcessingInstruction"
        elif (_g == 6):
            return "Document"
        else:
            pass
_Xml_XmlType_Impl_._hx_class = _Xml_XmlType_Impl_
_hx_classes["_Xml.XmlType_Impl_"] = _Xml_XmlType_Impl_


class Xml:
    _hx_class_name = "Xml"
    __slots__ = ("nodeType", "nodeName", "nodeValue", "parent", "children", "attributeMap")
    _hx_fields = ["nodeType", "nodeName", "nodeValue", "parent", "children", "attributeMap"]
    _hx_methods = ["get_nodeName", "set_nodeName", "get_nodeValue", "set_nodeValue", "get", "set", "remove", "exists", "attributes", "iterator", "elements", "elementsNamed", "firstChild", "firstElement", "addChild", "removeChild", "insertChild", "toString", "ensureElementType"]
    _hx_statics = ["Element", "PCData", "CData", "Comment", "DocType", "ProcessingInstruction", "Document", "parse", "createElement", "createPCData", "createCData", "createComment", "createDocType", "createProcessingInstruction", "createDocument"]

    def __init__(self,nodeType):
        self.parent = None
        self.nodeValue = None
        self.nodeName = None
        self.nodeType = nodeType
        self.children = []
        self.attributeMap = haxe_ds_StringMap()

    def get_nodeName(self):
        if (self.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        return self.nodeName

    def set_nodeName(self,v):
        if (self.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        def _hx_local_1():
            def _hx_local_0():
                self.nodeName = v
                return self.nodeName
            return _hx_local_0()
        return _hx_local_1()

    def get_nodeValue(self):
        if ((self.nodeType == Xml.Document) or ((self.nodeType == Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        return self.nodeValue

    def set_nodeValue(self,v):
        if ((self.nodeType == Xml.Document) or ((self.nodeType == Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        def _hx_local_1():
            def _hx_local_0():
                self.nodeValue = v
                return self.nodeValue
            return _hx_local_0()
        return _hx_local_1()

    def get(self,att):
        if (self.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        return self.attributeMap.h.get(att,None)

    def set(self,att,value):
        if (self.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        self.attributeMap.h[att] = value

    def remove(self,att):
        if (self.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        self.attributeMap.remove(att)

    def exists(self,att):
        if (self.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        return (att in self.attributeMap.h)

    def attributes(self):
        if (self.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        return self.attributeMap.keys()

    def iterator(self):
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        return haxe_iterators_ArrayIterator(self.children)

    def elements(self):
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        _g = []
        _g1 = 0
        _g2 = self.children
        while (_g1 < len(_g2)):
            child = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
            _g1 = (_g1 + 1)
            if (child.nodeType == Xml.Element):
                _g.append(child)
        ret = _g
        return haxe_iterators_ArrayIterator(ret)

    def elementsNamed(self,name):
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        _g = []
        _g1 = 0
        _g2 = self.children
        while (_g1 < len(_g2)):
            child = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
            _g1 = (_g1 + 1)
            tmp = None
            if (child.nodeType == Xml.Element):
                if (child.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((child.nodeType is None)) else _Xml_XmlType_Impl_.toString(child.nodeType))))))
                tmp = (child.nodeName == name)
            else:
                tmp = False
            if tmp:
                _g.append(child)
        ret = _g
        return haxe_iterators_ArrayIterator(ret)

    def firstChild(self):
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        return (self.children[0] if 0 < len(self.children) else None)

    def firstElement(self):
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        _g = 0
        _g1 = self.children
        while (_g < len(_g1)):
            child = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            if (child.nodeType == Xml.Element):
                return child
        return None

    def addChild(self,x):
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        if (x.parent is not None):
            x.parent.removeChild(x)
        _this = self.children
        _this.append(x)
        x.parent = self

    def removeChild(self,x):
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        if python_internal_ArrayImpl.remove(self.children,x):
            x.parent = None
            return True
        return False

    def insertChild(self,x,pos):
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        if (x.parent is not None):
            python_internal_ArrayImpl.remove(x.parent.children,x)
        self.children.insert(pos, x)
        x.parent = self

    def toString(self):
        return haxe_xml_Printer.print(self)

    def ensureElementType(self):
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))

    @staticmethod
    def parse(_hx_str):
        return haxe_xml_Parser.parse(_hx_str)

    @staticmethod
    def createElement(name):
        xml = Xml(Xml.Element)
        if (xml.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((xml.nodeType is None)) else _Xml_XmlType_Impl_.toString(xml.nodeType))))))
        xml.nodeName = name
        return xml

    @staticmethod
    def createPCData(data):
        xml = Xml(Xml.PCData)
        if ((xml.nodeType == Xml.Document) or ((xml.nodeType == Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((xml.nodeType is None)) else _Xml_XmlType_Impl_.toString(xml.nodeType))))))
        xml.nodeValue = data
        return xml

    @staticmethod
    def createCData(data):
        xml = Xml(Xml.CData)
        if ((xml.nodeType == Xml.Document) or ((xml.nodeType == Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((xml.nodeType is None)) else _Xml_XmlType_Impl_.toString(xml.nodeType))))))
        xml.nodeValue = data
        return xml

    @staticmethod
    def createComment(data):
        xml = Xml(Xml.Comment)
        if ((xml.nodeType == Xml.Document) or ((xml.nodeType == Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((xml.nodeType is None)) else _Xml_XmlType_Impl_.toString(xml.nodeType))))))
        xml.nodeValue = data
        return xml

    @staticmethod
    def createDocType(data):
        xml = Xml(Xml.DocType)
        if ((xml.nodeType == Xml.Document) or ((xml.nodeType == Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((xml.nodeType is None)) else _Xml_XmlType_Impl_.toString(xml.nodeType))))))
        xml.nodeValue = data
        return xml

    @staticmethod
    def createProcessingInstruction(data):
        xml = Xml(Xml.ProcessingInstruction)
        if ((xml.nodeType == Xml.Document) or ((xml.nodeType == Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((xml.nodeType is None)) else _Xml_XmlType_Impl_.toString(xml.nodeType))))))
        xml.nodeValue = data
        return xml

    @staticmethod
    def createDocument():
        return Xml(Xml.Document)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.nodeType = None
        _hx_o.parent = None
        _hx_o.children = None
        _hx_o.attributeMap = None
Xml._hx_class = Xml
_hx_classes["Xml"] = Xml

class haxe_StackItem(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.StackItem"
    _hx_constructs = ["CFunction", "Module", "FilePos", "Method", "LocalFunction"]

    @staticmethod
    def Module(m):
        return haxe_StackItem("Module", 1, (m,))

    @staticmethod
    def FilePos(s,file,line,column = None):
        return haxe_StackItem("FilePos", 2, (s,file,line,column))

    @staticmethod
    def Method(classname,method):
        return haxe_StackItem("Method", 3, (classname,method))

    @staticmethod
    def LocalFunction(v = None):
        return haxe_StackItem("LocalFunction", 4, (v,))
haxe_StackItem.CFunction = haxe_StackItem("CFunction", 0, ())
haxe_StackItem._hx_class = haxe_StackItem
_hx_classes["haxe.StackItem"] = haxe_StackItem


class haxe__CallStack_CallStack_Impl_:
    _hx_class_name = "haxe._CallStack.CallStack_Impl_"
    __slots__ = ()
    _hx_statics = ["get_length", "callStack", "exceptionStack", "toString", "subtract", "copy", "get", "asArray", "equalItems", "exceptionToString", "itemToString"]
    length = None

    @staticmethod
    def get_length(this1):
        return len(this1)

    @staticmethod
    def callStack():
        infos = python_lib_Traceback.extract_stack()
        if (len(infos) != 0):
            infos.pop()
        infos.reverse()
        return haxe_NativeStackTrace.toHaxe(infos)

    @staticmethod
    def exceptionStack(fullStack = None):
        if (fullStack is None):
            fullStack = False
        eStack = haxe_NativeStackTrace.toHaxe(haxe_NativeStackTrace.exceptionStack())
        return (eStack if fullStack else haxe__CallStack_CallStack_Impl_.subtract(eStack,haxe__CallStack_CallStack_Impl_.callStack()))

    @staticmethod
    def toString(stack):
        b = StringBuf()
        _g = 0
        _g1 = stack
        while (_g < len(_g1)):
            s = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            b.b.write("\nCalled from ")
            haxe__CallStack_CallStack_Impl_.itemToString(b,s)
        return b.b.getvalue()

    @staticmethod
    def subtract(this1,stack):
        startIndex = -1
        i = -1
        while True:
            i = (i + 1)
            tmp = i
            if (not ((tmp < len(this1)))):
                break
            _g = 0
            _g1 = len(stack)
            while (_g < _g1):
                j = _g
                _g = (_g + 1)
                if haxe__CallStack_CallStack_Impl_.equalItems((this1[i] if i >= 0 and i < len(this1) else None),python_internal_ArrayImpl._get(stack, j)):
                    if (startIndex < 0):
                        startIndex = i
                    i = (i + 1)
                    if (i >= len(this1)):
                        break
                else:
                    startIndex = -1
            if (startIndex >= 0):
                break
        if (startIndex >= 0):
            return this1[0:startIndex]
        else:
            return this1

    @staticmethod
    def copy(this1):
        return list(this1)

    @staticmethod
    def get(this1,index):
        return (this1[index] if index >= 0 and index < len(this1) else None)

    @staticmethod
    def asArray(this1):
        return this1

    @staticmethod
    def equalItems(item1,item2):
        if (item1 is None):
            if (item2 is None):
                return True
            else:
                return False
        else:
            tmp = item1.index
            if (tmp == 0):
                if (item2 is None):
                    return False
                elif (item2.index == 0):
                    return True
                else:
                    return False
            elif (tmp == 1):
                if (item2 is None):
                    return False
                elif (item2.index == 1):
                    m2 = item2.params[0]
                    m1 = item1.params[0]
                    return (m1 == m2)
                else:
                    return False
            elif (tmp == 2):
                if (item2 is None):
                    return False
                elif (item2.index == 2):
                    item21 = item2.params[0]
                    file2 = item2.params[1]
                    line2 = item2.params[2]
                    col2 = item2.params[3]
                    col1 = item1.params[3]
                    line1 = item1.params[2]
                    file1 = item1.params[1]
                    item11 = item1.params[0]
                    if (((file1 == file2) and ((line1 == line2))) and ((col1 == col2))):
                        return haxe__CallStack_CallStack_Impl_.equalItems(item11,item21)
                    else:
                        return False
                else:
                    return False
            elif (tmp == 3):
                if (item2 is None):
                    return False
                elif (item2.index == 3):
                    class2 = item2.params[0]
                    method2 = item2.params[1]
                    method1 = item1.params[1]
                    class1 = item1.params[0]
                    if (class1 == class2):
                        return (method1 == method2)
                    else:
                        return False
                else:
                    return False
            elif (tmp == 4):
                if (item2 is None):
                    return False
                elif (item2.index == 4):
                    v2 = item2.params[0]
                    v1 = item1.params[0]
                    return (v1 == v2)
                else:
                    return False
            else:
                pass

    @staticmethod
    def exceptionToString(e):
        if (e.get_previous() is None):
            tmp = ("Exception: " + HxOverrides.stringOrNull(e.toString()))
            tmp1 = e.get_stack()
            return (("null" if tmp is None else tmp) + HxOverrides.stringOrNull((("null" if ((tmp1 is None)) else haxe__CallStack_CallStack_Impl_.toString(tmp1)))))
        result = ""
        e1 = e
        prev = None
        while (e1 is not None):
            if (prev is None):
                result1 = ("Exception: " + HxOverrides.stringOrNull(e1.get_message()))
                tmp = e1.get_stack()
                result = ((("null" if result1 is None else result1) + HxOverrides.stringOrNull((("null" if ((tmp is None)) else haxe__CallStack_CallStack_Impl_.toString(tmp))))) + ("null" if result is None else result))
            else:
                prevStack = haxe__CallStack_CallStack_Impl_.subtract(e1.get_stack(),prev.get_stack())
                result = (((("Exception: " + HxOverrides.stringOrNull(e1.get_message())) + HxOverrides.stringOrNull((("null" if ((prevStack is None)) else haxe__CallStack_CallStack_Impl_.toString(prevStack))))) + "\n\nNext ") + ("null" if result is None else result))
            prev = e1
            e1 = e1.get_previous()
        return result

    @staticmethod
    def itemToString(b,s):
        tmp = s.index
        if (tmp == 0):
            b.b.write("a C function")
        elif (tmp == 1):
            m = s.params[0]
            b.b.write("module ")
            s1 = Std.string(m)
            b.b.write(s1)
        elif (tmp == 2):
            s1 = s.params[0]
            file = s.params[1]
            line = s.params[2]
            col = s.params[3]
            if (s1 is not None):
                haxe__CallStack_CallStack_Impl_.itemToString(b,s1)
                b.b.write(" (")
            s2 = Std.string(file)
            b.b.write(s2)
            b.b.write(" line ")
            s2 = Std.string(line)
            b.b.write(s2)
            if (col is not None):
                b.b.write(" column ")
                s2 = Std.string(col)
                b.b.write(s2)
            if (s1 is not None):
                b.b.write(")")
        elif (tmp == 3):
            cname = s.params[0]
            meth = s.params[1]
            s1 = Std.string(("<unknown>" if ((cname is None)) else cname))
            b.b.write(s1)
            b.b.write(".")
            s1 = Std.string(meth)
            b.b.write(s1)
        elif (tmp == 4):
            n = s.params[0]
            b.b.write("local function #")
            s = Std.string(n)
            b.b.write(s)
        else:
            pass
haxe__CallStack_CallStack_Impl_._hx_class = haxe__CallStack_CallStack_Impl_
_hx_classes["haxe._CallStack.CallStack_Impl_"] = haxe__CallStack_CallStack_Impl_


class haxe_IMap:
    _hx_class_name = "haxe.IMap"
    __slots__ = ()
    _hx_methods = ["get", "set", "exists", "remove", "keys", "iterator", "keyValueIterator", "copy", "toString", "clear"]
haxe_IMap._hx_class = haxe_IMap
_hx_classes["haxe.IMap"] = haxe_IMap


class haxe_Exception(Exception):
    _hx_class_name = "haxe.Exception"
    __slots__ = ("_hx___exceptionStack", "_hx___nativeStack", "_hx___skipStack", "_hx___nativeException", "_hx___previousException")
    _hx_fields = ["__exceptionStack", "__nativeStack", "__skipStack", "__nativeException", "__previousException"]
    _hx_methods = ["unwrap", "toString", "details", "__shiftStack", "get_message", "get_previous", "get_native", "get_stack"]
    _hx_statics = ["caught", "thrown"]
    _hx_interfaces = []
    _hx_super = Exception


    def __init__(self,message,previous = None,native = None):
        self._hx___previousException = None
        self._hx___nativeException = None
        self._hx___nativeStack = None
        self._hx___exceptionStack = None
        self._hx___skipStack = 0
        super().__init__(message)
        self._hx___previousException = previous
        if ((native is not None) and Std.isOfType(native,BaseException)):
            self._hx___nativeException = native
            self._hx___nativeStack = haxe_NativeStackTrace.exceptionStack()
        else:
            self._hx___nativeException = self
            infos = python_lib_Traceback.extract_stack()
            if (len(infos) != 0):
                infos.pop()
            infos.reverse()
            self._hx___nativeStack = infos

    def unwrap(self):
        return self._hx___nativeException

    def toString(self):
        return self.get_message()

    def details(self):
        if (self.get_previous() is None):
            tmp = ("Exception: " + HxOverrides.stringOrNull(self.toString()))
            tmp1 = self.get_stack()
            return (("null" if tmp is None else tmp) + HxOverrides.stringOrNull((("null" if ((tmp1 is None)) else haxe__CallStack_CallStack_Impl_.toString(tmp1)))))
        else:
            result = ""
            e = self
            prev = None
            while (e is not None):
                if (prev is None):
                    result1 = ("Exception: " + HxOverrides.stringOrNull(e.get_message()))
                    tmp = e.get_stack()
                    result = ((("null" if result1 is None else result1) + HxOverrides.stringOrNull((("null" if ((tmp is None)) else haxe__CallStack_CallStack_Impl_.toString(tmp))))) + ("null" if result is None else result))
                else:
                    prevStack = haxe__CallStack_CallStack_Impl_.subtract(e.get_stack(),prev.get_stack())
                    result = (((("Exception: " + HxOverrides.stringOrNull(e.get_message())) + HxOverrides.stringOrNull((("null" if ((prevStack is None)) else haxe__CallStack_CallStack_Impl_.toString(prevStack))))) + "\n\nNext ") + ("null" if result is None else result))
                prev = e
                e = e.get_previous()
            return result

    def _hx___shiftStack(self):
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0._hx___skipStack
        _hx_local_0._hx___skipStack = (_hx_local_1 + 1)
        _hx_local_1

    def get_message(self):
        return str(self)

    def get_previous(self):
        return self._hx___previousException

    def get_native(self):
        return self._hx___nativeException

    def get_stack(self):
        _g = self._hx___exceptionStack
        if (_g is None):
            def _hx_local_1():
                def _hx_local_0():
                    self._hx___exceptionStack = haxe_NativeStackTrace.toHaxe(self._hx___nativeStack,self._hx___skipStack)
                    return self._hx___exceptionStack
                return _hx_local_0()
            return _hx_local_1()
        else:
            s = _g
            return s

    @staticmethod
    def caught(value):
        if Std.isOfType(value,haxe_Exception):
            return value
        elif Std.isOfType(value,BaseException):
            return haxe_Exception(str(value),None,value)
        else:
            return haxe_ValueException(value,None,value)

    @staticmethod
    def thrown(value):
        if Std.isOfType(value,haxe_Exception):
            return value.get_native()
        elif Std.isOfType(value,BaseException):
            return value
        else:
            e = haxe_ValueException(value)
            e._hx___skipStack = (e._hx___skipStack + 1)
            return e

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o._hx___exceptionStack = None
        _hx_o._hx___nativeStack = None
        _hx_o._hx___skipStack = None
        _hx_o._hx___nativeException = None
        _hx_o._hx___previousException = None
haxe_Exception._hx_class = haxe_Exception
_hx_classes["haxe.Exception"] = haxe_Exception


class haxe__Int32_Int32_Impl_:
    _hx_class_name = "haxe._Int32.Int32_Impl_"
    __slots__ = ()
    _hx_statics = ["negate", "preIncrement", "postIncrement", "preDecrement", "postDecrement", "add", "addInt", "sub", "subInt", "intSub", "mul", "mulInt", "complement", "or", "orInt", "xor", "xorInt", "shr", "shrInt", "intShr", "shl", "shlInt", "intShl", "toFloat", "ucompare", "clamp"]

    @staticmethod
    def negate(this1):
        return (((~this1 + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def preIncrement(this1):
        this1 = (this1 + 1)
        x = this1
        this1 = ((x + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return this1

    @staticmethod
    def postIncrement(this1):
        ret = this1
        this1 = (this1 + 1)
        this1 = ((this1 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return ret

    @staticmethod
    def preDecrement(this1):
        this1 = (this1 - 1)
        x = this1
        this1 = ((x + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return this1

    @staticmethod
    def postDecrement(this1):
        ret = this1
        this1 = (this1 - 1)
        this1 = ((this1 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return ret

    @staticmethod
    def add(a,b):
        return (((a + b) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def addInt(a,b):
        return (((a + b) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def sub(a,b):
        return (((a - b) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def subInt(a,b):
        return (((a - b) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def intSub(a,b):
        return (((a - b) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def mul(a,b):
        return ((((a * ((b & 65535))) + ((((((a * (HxOverrides.rshift(b, 16))) << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def mulInt(a,b):
        return haxe__Int32_Int32_Impl_.mul(a,b)

    @staticmethod
    def complement(a):
        return ((~a + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def _hx_or(a,b):
        return ((((a | b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def orInt(a,b):
        return ((((a | b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def xor(a,b):
        return ((((a ^ b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def xorInt(a,b):
        return ((((a ^ b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def shr(a,b):
        return ((((a >> b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def shrInt(a,b):
        return ((((a >> b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def intShr(a,b):
        return ((((a >> b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def shl(a,b):
        return ((((a << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def shlInt(a,b):
        return ((((a << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def intShl(a,b):
        return ((((a << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def toFloat(this1):
        return this1

    @staticmethod
    def ucompare(a,b):
        if (a < 0):
            if (b < 0):
                return (((((~b + (2 ** 31)) % (2 ** 32) - (2 ** 31)) - (((~a + (2 ** 31)) % (2 ** 32) - (2 ** 31)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            else:
                return 1
        if (b < 0):
            return -1
        else:
            return (((a - b) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def clamp(x):
        return ((x + (2 ** 31)) % (2 ** 32) - (2 ** 31))
haxe__Int32_Int32_Impl_._hx_class = haxe__Int32_Int32_Impl_
_hx_classes["haxe._Int32.Int32_Impl_"] = haxe__Int32_Int32_Impl_


class haxe__Int64_Int64_Impl_:
    _hx_class_name = "haxe._Int64.Int64_Impl_"
    __slots__ = ()
    _hx_statics = ["_new", "copy", "make", "ofInt", "toInt", "is", "isInt64", "getHigh", "getLow", "isNeg", "isZero", "compare", "ucompare", "toStr", "toString", "parseString", "fromFloat", "divMod", "neg", "preIncrement", "postIncrement", "preDecrement", "postDecrement", "add", "addInt", "sub", "subInt", "intSub", "mul", "mulInt", "div", "divInt", "intDiv", "mod", "modInt", "intMod", "eq", "eqInt", "neq", "neqInt", "lt", "ltInt", "intLt", "lte", "lteInt", "intLte", "gt", "gtInt", "intGt", "gte", "gteInt", "intGte", "complement", "and", "or", "xor", "shl", "shr", "ushr", "get_high", "set_high", "get_low", "set_low"]
    high = None
    low = None

    @staticmethod
    def _new(x):
        this1 = x
        return this1

    @staticmethod
    def copy(this1):
        this2 = haxe__Int64____Int64(this1.high,this1.low)
        return this2

    @staticmethod
    def make(high,low):
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def ofInt(x):
        this1 = haxe__Int64____Int64((x >> 31),x)
        return this1

    @staticmethod
    def toInt(x):
        if (x.high != ((((x.low >> 31)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))):
            raise haxe_Exception.thrown("Overflow")
        return x.low

    @staticmethod
    def _hx_is(val):
        return Std.isOfType(val,haxe__Int64____Int64)

    @staticmethod
    def isInt64(val):
        return Std.isOfType(val,haxe__Int64____Int64)

    @staticmethod
    def getHigh(x):
        return x.high

    @staticmethod
    def getLow(x):
        return x.low

    @staticmethod
    def isNeg(x):
        return (x.high < 0)

    @staticmethod
    def isZero(x):
        b_high = 0
        b_low = 0
        if (x.high == b_high):
            return (x.low == b_low)
        else:
            return False

    @staticmethod
    def compare(a,b):
        v = (((a.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b.low)
        if (a.high < 0):
            if (b.high < 0):
                return v
            else:
                return -1
        elif (b.high >= 0):
            return v
        else:
            return 1

    @staticmethod
    def ucompare(a,b):
        v = haxe__Int32_Int32_Impl_.ucompare(a.high,b.high)
        if (v != 0):
            return v
        else:
            return haxe__Int32_Int32_Impl_.ucompare(a.low,b.low)

    @staticmethod
    def toStr(x):
        return haxe__Int64_Int64_Impl_.toString(x)

    @staticmethod
    def toString(this1):
        i = this1
        b_high = 0
        b_low = 0
        if ((i.high == b_high) and ((i.low == b_low))):
            return "0"
        _hx_str = ""
        neg = False
        if (i.high < 0):
            neg = True
        this1 = haxe__Int64____Int64(0,10)
        ten = this1
        while True:
            b_high = 0
            b_low = 0
            if (not (((i.high != b_high) or ((i.low != b_low))))):
                break
            r = haxe__Int64_Int64_Impl_.divMod(i,ten)
            if (r.modulus.high < 0):
                x = r.modulus
                high = ((~x.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                low = (((~x.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                if (low == 0):
                    ret = high
                    high = (high + 1)
                    high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                this_high = high
                this_low = low
                _hx_str = (Std.string(this_low) + ("null" if _hx_str is None else _hx_str))
                x1 = r.quotient
                high1 = ((~x1.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                low1 = (((~x1.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                if (low1 == 0):
                    ret1 = high1
                    high1 = (high1 + 1)
                    high1 = ((high1 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                this1 = haxe__Int64____Int64(high1,low1)
                i = this1
            else:
                _hx_str = (Std.string(r.modulus.low) + ("null" if _hx_str is None else _hx_str))
                i = r.quotient
        if neg:
            _hx_str = ("-" + ("null" if _hx_str is None else _hx_str))
        return _hx_str

    @staticmethod
    def parseString(sParam):
        return haxe_Int64Helper.parseString(sParam)

    @staticmethod
    def fromFloat(f):
        return haxe_Int64Helper.fromFloat(f)

    @staticmethod
    def divMod(dividend,divisor):
        if (divisor.high == 0):
            _g = divisor.low
            if (_g == 0):
                raise haxe_Exception.thrown("divide by zero")
            elif (_g == 1):
                this1 = haxe__Int64____Int64(dividend.high,dividend.low)
                this2 = haxe__Int64____Int64(0,0)
                return _hx_AnonObject({'quotient': this1, 'modulus': this2})
            else:
                pass
        divSign = ((dividend.high < 0) != ((divisor.high < 0)))
        modulus = None
        if (dividend.high < 0):
            high = ((~dividend.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            low = (((~dividend.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            if (low == 0):
                ret = high
                high = (high + 1)
                high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            this1 = haxe__Int64____Int64(high,low)
            modulus = this1
        else:
            this1 = haxe__Int64____Int64(dividend.high,dividend.low)
            modulus = this1
        if (divisor.high < 0):
            high = ((~divisor.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            low = (((~divisor.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            if (low == 0):
                ret = high
                high = (high + 1)
                high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            this1 = haxe__Int64____Int64(high,low)
            divisor = this1
        this1 = haxe__Int64____Int64(0,0)
        quotient = this1
        this1 = haxe__Int64____Int64(0,1)
        mask = this1
        while (not ((divisor.high < 0))):
            v = haxe__Int32_Int32_Impl_.ucompare(divisor.high,modulus.high)
            cmp = (v if ((v != 0)) else haxe__Int32_Int32_Impl_.ucompare(divisor.low,modulus.low))
            b = 1
            b = (b & 63)
            if (b == 0):
                this1 = haxe__Int64____Int64(divisor.high,divisor.low)
                divisor = this1
            elif (b < 32):
                this2 = haxe__Int64____Int64(((((((((divisor.high << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(divisor.low, ((32 - b))))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((divisor.low << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
                divisor = this2
            else:
                this3 = haxe__Int64____Int64(((((divisor.low << ((b - 32)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),0)
                divisor = this3
            b1 = 1
            b1 = (b1 & 63)
            if (b1 == 0):
                this4 = haxe__Int64____Int64(mask.high,mask.low)
                mask = this4
            elif (b1 < 32):
                this5 = haxe__Int64____Int64(((((((((mask.high << b1)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(mask.low, ((32 - b1))))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((mask.low << b1)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
                mask = this5
            else:
                this6 = haxe__Int64____Int64(((((mask.low << ((b1 - 32)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),0)
                mask = this6
            if (cmp >= 0):
                break
        while True:
            b_high = 0
            b_low = 0
            if (not (((mask.high != b_high) or ((mask.low != b_low))))):
                break
            v = haxe__Int32_Int32_Impl_.ucompare(modulus.high,divisor.high)
            if (((v if ((v != 0)) else haxe__Int32_Int32_Impl_.ucompare(modulus.low,divisor.low))) >= 0):
                this1 = haxe__Int64____Int64(((((quotient.high | mask.high)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((quotient.low | mask.low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
                quotient = this1
                high = (((modulus.high - divisor.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                low = (((modulus.low - divisor.low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                if (haxe__Int32_Int32_Impl_.ucompare(modulus.low,divisor.low) < 0):
                    ret = high
                    high = (high - 1)
                    high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                this2 = haxe__Int64____Int64(high,low)
                modulus = this2
            b = 1
            b = (b & 63)
            if (b == 0):
                this3 = haxe__Int64____Int64(mask.high,mask.low)
                mask = this3
            elif (b < 32):
                this4 = haxe__Int64____Int64(HxOverrides.rshift(mask.high, b),((((((((mask.high << ((32 - b)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(mask.low, b))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
                mask = this4
            else:
                this5 = haxe__Int64____Int64(0,HxOverrides.rshift(mask.high, ((b - 32))))
                mask = this5
            b1 = 1
            b1 = (b1 & 63)
            if (b1 == 0):
                this6 = haxe__Int64____Int64(divisor.high,divisor.low)
                divisor = this6
            elif (b1 < 32):
                this7 = haxe__Int64____Int64(HxOverrides.rshift(divisor.high, b1),((((((((divisor.high << ((32 - b1)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(divisor.low, b1))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
                divisor = this7
            else:
                this8 = haxe__Int64____Int64(0,HxOverrides.rshift(divisor.high, ((b1 - 32))))
                divisor = this8
        if divSign:
            high = ((~quotient.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            low = (((~quotient.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            if (low == 0):
                ret = high
                high = (high + 1)
                high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            this1 = haxe__Int64____Int64(high,low)
            quotient = this1
        if (dividend.high < 0):
            high = ((~modulus.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            low = (((~modulus.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            if (low == 0):
                ret = high
                high = (high + 1)
                high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            this1 = haxe__Int64____Int64(high,low)
            modulus = this1
        return _hx_AnonObject({'quotient': quotient, 'modulus': modulus})

    @staticmethod
    def neg(x):
        high = ((~x.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((~x.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (low == 0):
            ret = high
            high = (high + 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def preIncrement(this1):
        this2 = haxe__Int64____Int64(this1.high,this1.low)
        this1 = this2
        def _hx_local_1():
            _hx_local_0 = this1.low
            this1.low = (this1.low + 1)
            return _hx_local_0
        ret = _hx_local_1()
        this1.low = ((this1.low + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (this1.low == 0):
            def _hx_local_3():
                _hx_local_2 = this1.high
                this1.high = (this1.high + 1)
                return _hx_local_2
            ret = _hx_local_3()
            this1.high = ((this1.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return this1

    @staticmethod
    def postIncrement(this1):
        ret = this1
        this2 = haxe__Int64____Int64(this1.high,this1.low)
        this1 = this2
        def _hx_local_2():
            _hx_local_0 = this1
            _hx_local_1 = _hx_local_0.low
            _hx_local_0.low = (_hx_local_1 + 1)
            return _hx_local_1
        ret1 = _hx_local_2()
        this1.low = ((this1.low + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (this1.low == 0):
            def _hx_local_5():
                _hx_local_3 = this1
                _hx_local_4 = _hx_local_3.high
                _hx_local_3.high = (_hx_local_4 + 1)
                return _hx_local_4
            ret1 = _hx_local_5()
            this1.high = ((this1.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return ret

    @staticmethod
    def preDecrement(this1):
        this2 = haxe__Int64____Int64(this1.high,this1.low)
        this1 = this2
        if (this1.low == 0):
            def _hx_local_1():
                _hx_local_0 = this1.high
                this1.high = (this1.high - 1)
                return _hx_local_0
            ret = _hx_local_1()
            this1.high = ((this1.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        def _hx_local_3():
            _hx_local_2 = this1.low
            this1.low = (this1.low - 1)
            return _hx_local_2
        ret = _hx_local_3()
        this1.low = ((this1.low + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return this1

    @staticmethod
    def postDecrement(this1):
        ret = this1
        this2 = haxe__Int64____Int64(this1.high,this1.low)
        this1 = this2
        if (this1.low == 0):
            def _hx_local_2():
                _hx_local_0 = this1
                _hx_local_1 = _hx_local_0.high
                _hx_local_0.high = (_hx_local_1 - 1)
                return _hx_local_1
            ret1 = _hx_local_2()
            this1.high = ((this1.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        def _hx_local_5():
            _hx_local_3 = this1
            _hx_local_4 = _hx_local_3.low
            _hx_local_3.low = (_hx_local_4 - 1)
            return _hx_local_4
        ret1 = _hx_local_5()
        this1.low = ((this1.low + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return ret

    @staticmethod
    def add(a,b):
        high = (((a.high + b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((a.low + b.low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(low,a.low) < 0):
            ret = high
            high = (high + 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def addInt(a,b):
        b_high = (b >> 31)
        b_low = b
        high = (((a.high + b_high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((a.low + b_low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(low,a.low) < 0):
            ret = high
            high = (high + 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def sub(a,b):
        high = (((a.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((a.low - b.low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(a.low,b.low) < 0):
            ret = high
            high = (high - 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def subInt(a,b):
        b_high = (b >> 31)
        b_low = b
        high = (((a.high - b_high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((a.low - b_low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(a.low,b_low) < 0):
            ret = high
            high = (high - 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def intSub(a,b):
        a_high = (a >> 31)
        a_low = a
        high = (((a_high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((a_low - b.low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(a_low,b.low) < 0):
            ret = high
            high = (high - 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def mul(a,b):
        mask = 65535
        al = (a.low & mask)
        ah = HxOverrides.rshift(a.low, 16)
        bl = (b.low & mask)
        bh = HxOverrides.rshift(b.low, 16)
        p00 = haxe__Int32_Int32_Impl_.mul(al,bl)
        p10 = haxe__Int32_Int32_Impl_.mul(ah,bl)
        p01 = haxe__Int32_Int32_Impl_.mul(al,bh)
        p11 = haxe__Int32_Int32_Impl_.mul(ah,bh)
        low = p00
        high = ((((((p11 + (HxOverrides.rshift(p01, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) + (HxOverrides.rshift(p10, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        p01 = ((((p01 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((low + p01) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(low,p01) < 0):
            ret = high
            high = (high + 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        p10 = ((((p10 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((low + p10) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(low,p10) < 0):
            ret = high
            high = (high + 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        high = (((high + ((((haxe__Int32_Int32_Impl_.mul(a.low,b.high) + haxe__Int32_Int32_Impl_.mul(a.high,b.low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def mulInt(a,b):
        b_high = (b >> 31)
        b_low = b
        mask = 65535
        al = (a.low & mask)
        ah = HxOverrides.rshift(a.low, 16)
        bl = (b_low & mask)
        bh = HxOverrides.rshift(b_low, 16)
        p00 = haxe__Int32_Int32_Impl_.mul(al,bl)
        p10 = haxe__Int32_Int32_Impl_.mul(ah,bl)
        p01 = haxe__Int32_Int32_Impl_.mul(al,bh)
        p11 = haxe__Int32_Int32_Impl_.mul(ah,bh)
        low = p00
        high = ((((((p11 + (HxOverrides.rshift(p01, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) + (HxOverrides.rshift(p10, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        p01 = ((((p01 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((low + p01) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(low,p01) < 0):
            ret = high
            high = (high + 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        p10 = ((((p10 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((low + p10) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(low,p10) < 0):
            ret = high
            high = (high + 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        high = (((high + ((((haxe__Int32_Int32_Impl_.mul(a.low,b_high) + haxe__Int32_Int32_Impl_.mul(a.high,b_low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def div(a,b):
        return haxe__Int64_Int64_Impl_.divMod(a,b).quotient

    @staticmethod
    def divInt(a,b):
        this1 = haxe__Int64____Int64((b >> 31),b)
        return haxe__Int64_Int64_Impl_.divMod(a,this1).quotient

    @staticmethod
    def intDiv(a,b):
        this1 = haxe__Int64____Int64((a >> 31),a)
        x = haxe__Int64_Int64_Impl_.divMod(this1,b).quotient
        if (x.high != ((((x.low >> 31)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))):
            raise haxe_Exception.thrown("Overflow")
        x1 = x.low
        this1 = haxe__Int64____Int64((x1 >> 31),x1)
        return this1

    @staticmethod
    def mod(a,b):
        return haxe__Int64_Int64_Impl_.divMod(a,b).modulus

    @staticmethod
    def modInt(a,b):
        this1 = haxe__Int64____Int64((b >> 31),b)
        x = haxe__Int64_Int64_Impl_.divMod(a,this1).modulus
        if (x.high != ((((x.low >> 31)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))):
            raise haxe_Exception.thrown("Overflow")
        x1 = x.low
        this1 = haxe__Int64____Int64((x1 >> 31),x1)
        return this1

    @staticmethod
    def intMod(a,b):
        this1 = haxe__Int64____Int64((a >> 31),a)
        x = haxe__Int64_Int64_Impl_.divMod(this1,b).modulus
        if (x.high != ((((x.low >> 31)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))):
            raise haxe_Exception.thrown("Overflow")
        x1 = x.low
        this1 = haxe__Int64____Int64((x1 >> 31),x1)
        return this1

    @staticmethod
    def eq(a,b):
        if (a.high == b.high):
            return (a.low == b.low)
        else:
            return False

    @staticmethod
    def eqInt(a,b):
        b_high = (b >> 31)
        b_low = b
        if (a.high == b_high):
            return (a.low == b_low)
        else:
            return False

    @staticmethod
    def neq(a,b):
        if (a.high == b.high):
            return (a.low != b.low)
        else:
            return True

    @staticmethod
    def neqInt(a,b):
        b_high = (b >> 31)
        b_low = b
        if (a.high == b_high):
            return (a.low != b_low)
        else:
            return True

    @staticmethod
    def lt(a,b):
        v = (((a.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a.high < 0)) else (v if ((b.high >= 0)) else 1))) < 0)

    @staticmethod
    def ltInt(a,b):
        b_high = (b >> 31)
        b_low = b
        v = (((a.high - b_high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b_low)
        return ((((v if ((b_high < 0)) else -1) if ((a.high < 0)) else (v if ((b_high >= 0)) else 1))) < 0)

    @staticmethod
    def intLt(a,b):
        a_high = (a >> 31)
        a_low = a
        v = (((a_high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a_low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a_high < 0)) else (v if ((b.high >= 0)) else 1))) < 0)

    @staticmethod
    def lte(a,b):
        v = (((a.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a.high < 0)) else (v if ((b.high >= 0)) else 1))) <= 0)

    @staticmethod
    def lteInt(a,b):
        b_high = (b >> 31)
        b_low = b
        v = (((a.high - b_high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b_low)
        return ((((v if ((b_high < 0)) else -1) if ((a.high < 0)) else (v if ((b_high >= 0)) else 1))) <= 0)

    @staticmethod
    def intLte(a,b):
        a_high = (a >> 31)
        a_low = a
        v = (((a_high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a_low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a_high < 0)) else (v if ((b.high >= 0)) else 1))) <= 0)

    @staticmethod
    def gt(a,b):
        v = (((a.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a.high < 0)) else (v if ((b.high >= 0)) else 1))) > 0)

    @staticmethod
    def gtInt(a,b):
        b_high = (b >> 31)
        b_low = b
        v = (((a.high - b_high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b_low)
        return ((((v if ((b_high < 0)) else -1) if ((a.high < 0)) else (v if ((b_high >= 0)) else 1))) > 0)

    @staticmethod
    def intGt(a,b):
        a_high = (a >> 31)
        a_low = a
        v = (((a_high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a_low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a_high < 0)) else (v if ((b.high >= 0)) else 1))) > 0)

    @staticmethod
    def gte(a,b):
        v = (((a.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a.high < 0)) else (v if ((b.high >= 0)) else 1))) >= 0)

    @staticmethod
    def gteInt(a,b):
        b_high = (b >> 31)
        b_low = b
        v = (((a.high - b_high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b_low)
        return ((((v if ((b_high < 0)) else -1) if ((a.high < 0)) else (v if ((b_high >= 0)) else 1))) >= 0)

    @staticmethod
    def intGte(a,b):
        a_high = (a >> 31)
        a_low = a
        v = (((a_high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a_low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a_high < 0)) else (v if ((b.high >= 0)) else 1))) >= 0)

    @staticmethod
    def complement(a):
        this1 = haxe__Int64____Int64(((~a.high + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((~a.low + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
        return this1

    @staticmethod
    def _hx_and(a,b):
        this1 = haxe__Int64____Int64((a.high & b.high),(a.low & b.low))
        return this1

    @staticmethod
    def _hx_or(a,b):
        this1 = haxe__Int64____Int64(((((a.high | b.high)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((a.low | b.low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
        return this1

    @staticmethod
    def xor(a,b):
        this1 = haxe__Int64____Int64(((((a.high ^ b.high)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((a.low ^ b.low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
        return this1

    @staticmethod
    def shl(a,b):
        b = (b & 63)
        if (b == 0):
            this1 = haxe__Int64____Int64(a.high,a.low)
            return this1
        elif (b < 32):
            this1 = haxe__Int64____Int64(((((((((a.high << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(a.low, ((32 - b))))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((a.low << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
            return this1
        else:
            this1 = haxe__Int64____Int64(((((a.low << ((b - 32)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),0)
            return this1

    @staticmethod
    def shr(a,b):
        b = (b & 63)
        if (b == 0):
            this1 = haxe__Int64____Int64(a.high,a.low)
            return this1
        elif (b < 32):
            this1 = haxe__Int64____Int64(((((a.high >> b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((((((a.high << ((32 - b)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(a.low, b))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
            return this1
        else:
            this1 = haxe__Int64____Int64(((((a.high >> 31)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((a.high >> ((b - 32)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
            return this1

    @staticmethod
    def ushr(a,b):
        b = (b & 63)
        if (b == 0):
            this1 = haxe__Int64____Int64(a.high,a.low)
            return this1
        elif (b < 32):
            this1 = haxe__Int64____Int64(HxOverrides.rshift(a.high, b),((((((((a.high << ((32 - b)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(a.low, b))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
            return this1
        else:
            this1 = haxe__Int64____Int64(0,HxOverrides.rshift(a.high, ((b - 32))))
            return this1

    @staticmethod
    def get_high(this1):
        return this1.high

    @staticmethod
    def set_high(this1,x):
        def _hx_local_1():
            def _hx_local_0():
                this1.high = x
                return this1.high
            return _hx_local_0()
        return _hx_local_1()

    @staticmethod
    def get_low(this1):
        return this1.low

    @staticmethod
    def set_low(this1,x):
        def _hx_local_1():
            def _hx_local_0():
                this1.low = x
                return this1.low
            return _hx_local_0()
        return _hx_local_1()
haxe__Int64_Int64_Impl_._hx_class = haxe__Int64_Int64_Impl_
_hx_classes["haxe._Int64.Int64_Impl_"] = haxe__Int64_Int64_Impl_


class haxe__Int64____Int64:
    _hx_class_name = "haxe._Int64.___Int64"
    __slots__ = ("high", "low")
    _hx_fields = ["high", "low"]
    _hx_methods = ["toString"]

    def __init__(self,high,low):
        self.high = high
        self.low = low

    def toString(self):
        return haxe__Int64_Int64_Impl_.toString(self)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.high = None
        _hx_o.low = None
haxe__Int64____Int64._hx_class = haxe__Int64____Int64
_hx_classes["haxe._Int64.___Int64"] = haxe__Int64____Int64


class haxe_Int64Helper:
    _hx_class_name = "haxe.Int64Helper"
    __slots__ = ()
    _hx_statics = ["parseString", "fromFloat"]

    @staticmethod
    def parseString(sParam):
        base_high = 0
        base_low = 10
        this1 = haxe__Int64____Int64(0,0)
        current = this1
        this1 = haxe__Int64____Int64(0,1)
        multiplier = this1
        sIsNegative = False
        s = StringTools.trim(sParam)
        if ((("" if ((0 >= len(s))) else s[0])) == "-"):
            sIsNegative = True
            s = HxString.substring(s,1,len(s))
        _hx_len = len(s)
        _g = 0
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            digitInt = (HxString.charCodeAt(s,((_hx_len - 1) - i)) - 48)
            if ((digitInt < 0) or ((digitInt > 9))):
                raise haxe_Exception.thrown("NumberFormatError")
            if (digitInt != 0):
                digit_high = (digitInt >> 31)
                digit_low = digitInt
                if sIsNegative:
                    mask = 65535
                    al = (multiplier.low & mask)
                    ah = HxOverrides.rshift(multiplier.low, 16)
                    bl = (digit_low & mask)
                    bh = HxOverrides.rshift(digit_low, 16)
                    p00 = haxe__Int32_Int32_Impl_.mul(al,bl)
                    p10 = haxe__Int32_Int32_Impl_.mul(ah,bl)
                    p01 = haxe__Int32_Int32_Impl_.mul(al,bh)
                    p11 = haxe__Int32_Int32_Impl_.mul(ah,bh)
                    low = p00
                    high = ((((((p11 + (HxOverrides.rshift(p01, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) + (HxOverrides.rshift(p10, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    p01 = ((((p01 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    low = (((low + p01) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    if (haxe__Int32_Int32_Impl_.ucompare(low,p01) < 0):
                        ret = high
                        high = (high + 1)
                        high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    p10 = ((((p10 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    low = (((low + p10) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    if (haxe__Int32_Int32_Impl_.ucompare(low,p10) < 0):
                        ret1 = high
                        high = (high + 1)
                        high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    high = (((high + ((((haxe__Int32_Int32_Impl_.mul(multiplier.low,digit_high) + haxe__Int32_Int32_Impl_.mul(multiplier.high,digit_low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    b_high = high
                    b_low = low
                    high1 = (((current.high - b_high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    low1 = (((current.low - b_low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    if (haxe__Int32_Int32_Impl_.ucompare(current.low,b_low) < 0):
                        ret2 = high1
                        high1 = (high1 - 1)
                        high1 = ((high1 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    this1 = haxe__Int64____Int64(high1,low1)
                    current = this1
                    if (not ((current.high < 0))):
                        raise haxe_Exception.thrown("NumberFormatError: Underflow")
                else:
                    mask1 = 65535
                    al1 = (multiplier.low & mask1)
                    ah1 = HxOverrides.rshift(multiplier.low, 16)
                    bl1 = (digit_low & mask1)
                    bh1 = HxOverrides.rshift(digit_low, 16)
                    p001 = haxe__Int32_Int32_Impl_.mul(al1,bl1)
                    p101 = haxe__Int32_Int32_Impl_.mul(ah1,bl1)
                    p011 = haxe__Int32_Int32_Impl_.mul(al1,bh1)
                    p111 = haxe__Int32_Int32_Impl_.mul(ah1,bh1)
                    low2 = p001
                    high2 = ((((((p111 + (HxOverrides.rshift(p011, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) + (HxOverrides.rshift(p101, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    p011 = ((((p011 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    low2 = (((low2 + p011) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    if (haxe__Int32_Int32_Impl_.ucompare(low2,p011) < 0):
                        ret3 = high2
                        high2 = (high2 + 1)
                        high2 = ((high2 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    p101 = ((((p101 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    low2 = (((low2 + p101) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    if (haxe__Int32_Int32_Impl_.ucompare(low2,p101) < 0):
                        ret4 = high2
                        high2 = (high2 + 1)
                        high2 = ((high2 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    high2 = (((high2 + ((((haxe__Int32_Int32_Impl_.mul(multiplier.low,digit_high) + haxe__Int32_Int32_Impl_.mul(multiplier.high,digit_low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    b_high1 = high2
                    b_low1 = low2
                    high3 = (((current.high + b_high1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    low3 = (((current.low + b_low1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    if (haxe__Int32_Int32_Impl_.ucompare(low3,current.low) < 0):
                        ret5 = high3
                        high3 = (high3 + 1)
                        high3 = ((high3 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    this2 = haxe__Int64____Int64(high3,low3)
                    current = this2
                    if (current.high < 0):
                        raise haxe_Exception.thrown("NumberFormatError: Overflow")
            mask2 = 65535
            al2 = (multiplier.low & mask2)
            ah2 = HxOverrides.rshift(multiplier.low, 16)
            bl2 = (base_low & mask2)
            bh2 = HxOverrides.rshift(base_low, 16)
            p002 = haxe__Int32_Int32_Impl_.mul(al2,bl2)
            p102 = haxe__Int32_Int32_Impl_.mul(ah2,bl2)
            p012 = haxe__Int32_Int32_Impl_.mul(al2,bh2)
            p112 = haxe__Int32_Int32_Impl_.mul(ah2,bh2)
            low4 = p002
            high4 = ((((((p112 + (HxOverrides.rshift(p012, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) + (HxOverrides.rshift(p102, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            p012 = ((((p012 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            low4 = (((low4 + p012) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            if (haxe__Int32_Int32_Impl_.ucompare(low4,p012) < 0):
                ret6 = high4
                high4 = (high4 + 1)
                high4 = ((high4 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            p102 = ((((p102 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            low4 = (((low4 + p102) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            if (haxe__Int32_Int32_Impl_.ucompare(low4,p102) < 0):
                ret7 = high4
                high4 = (high4 + 1)
                high4 = ((high4 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            high4 = (((high4 + ((((haxe__Int32_Int32_Impl_.mul(multiplier.low,base_high) + haxe__Int32_Int32_Impl_.mul(multiplier.high,base_low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            this3 = haxe__Int64____Int64(high4,low4)
            multiplier = this3
        return current

    @staticmethod
    def fromFloat(f):
        if (python_lib_Math.isnan(f) or (not ((((f != Math.POSITIVE_INFINITY) and ((f != Math.NEGATIVE_INFINITY))) and (not python_lib_Math.isnan(f)))))):
            raise haxe_Exception.thrown("Number is NaN or Infinite")
        noFractions = (f - (HxOverrides.modf(f, 1)))
        if (noFractions > 9007199254740991):
            raise haxe_Exception.thrown("Conversion overflow")
        if (noFractions < -9007199254740991):
            raise haxe_Exception.thrown("Conversion underflow")
        this1 = haxe__Int64____Int64(0,0)
        result = this1
        neg = (noFractions < 0)
        rest = (-noFractions if neg else noFractions)
        i = 0
        while (rest >= 1):
            curr = HxOverrides.modf(rest, 2)
            rest = (rest / 2)
            if (curr >= 1):
                a_high = 0
                a_low = 1
                b = i
                b = (b & 63)
                b1 = None
                if (b == 0):
                    this1 = haxe__Int64____Int64(a_high,a_low)
                    b1 = this1
                elif (b < 32):
                    this2 = haxe__Int64____Int64(((((((((a_high << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(a_low, ((32 - b))))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((a_low << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
                    b1 = this2
                else:
                    this3 = haxe__Int64____Int64(((((a_low << ((b - 32)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),0)
                    b1 = this3
                high = (((result.high + b1.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                low = (((result.low + b1.low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                if (haxe__Int32_Int32_Impl_.ucompare(low,result.low) < 0):
                    ret = high
                    high = (high + 1)
                    high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                this4 = haxe__Int64____Int64(high,low)
                result = this4
            i = (i + 1)
        if neg:
            high = ((~result.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            low = (((~result.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            if (low == 0):
                ret = high
                high = (high + 1)
                high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            this1 = haxe__Int64____Int64(high,low)
            result = this1
        return result
haxe_Int64Helper._hx_class = haxe_Int64Helper
_hx_classes["haxe.Int64Helper"] = haxe_Int64Helper


class haxe_Json:
    _hx_class_name = "haxe.Json"
    __slots__ = ()
    _hx_statics = ["parse", "stringify"]

    @staticmethod
    def parse(text):
        return python_lib_Json.loads(text,**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'object_hook': python_Lib.dictToAnon})))

    @staticmethod
    def stringify(value,replacer = None,space = None):
        return haxe_format_JsonPrinter.print(value,replacer,space)
haxe_Json._hx_class = haxe_Json
_hx_classes["haxe.Json"] = haxe_Json


class haxe_Log:
    _hx_class_name = "haxe.Log"
    __slots__ = ()
    _hx_statics = ["formatOutput", "trace"]

    @staticmethod
    def formatOutput(v,infos):
        _hx_str = Std.string(v)
        if (infos is None):
            return _hx_str
        pstr = ((HxOverrides.stringOrNull(infos.fileName) + ":") + Std.string(infos.lineNumber))
        if (Reflect.field(infos,"customParams") is not None):
            _g = 0
            _g1 = Reflect.field(infos,"customParams")
            while (_g < len(_g1)):
                v = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                _hx_str = (("null" if _hx_str is None else _hx_str) + ((", " + Std.string(v))))
        return ((("null" if pstr is None else pstr) + ": ") + ("null" if _hx_str is None else _hx_str))

    @staticmethod
    def trace(v,infos = None):
        _hx_str = haxe_Log.formatOutput(v,infos)
        str1 = Std.string(_hx_str)
        python_Lib.printString((("" + ("null" if str1 is None else str1)) + HxOverrides.stringOrNull(python_Lib.lineEnd)))
haxe_Log._hx_class = haxe_Log
_hx_classes["haxe.Log"] = haxe_Log


class haxe_NativeStackTrace:
    _hx_class_name = "haxe.NativeStackTrace"
    __slots__ = ()
    _hx_statics = ["saveStack", "callStack", "exceptionStack", "toHaxe"]

    @staticmethod
    def saveStack(exception):
        pass

    @staticmethod
    def callStack():
        infos = python_lib_Traceback.extract_stack()
        if (len(infos) != 0):
            infos.pop()
        infos.reverse()
        return infos

    @staticmethod
    def exceptionStack():
        exc = python_lib_Sys.exc_info()
        if (exc[2] is not None):
            infos = python_lib_Traceback.extract_tb(exc[2])
            infos.reverse()
            return infos
        else:
            return []

    @staticmethod
    def toHaxe(native,skip = None):
        if (skip is None):
            skip = 0
        stack = []
        _g = 0
        _g1 = len(native)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (skip > i):
                continue
            elem = (native[i] if i >= 0 and i < len(native) else None)
            x = haxe_StackItem.FilePos(haxe_StackItem.Method(None,elem[2]),elem[0],elem[1])
            stack.append(x)
        return stack
haxe_NativeStackTrace._hx_class = haxe_NativeStackTrace
_hx_classes["haxe.NativeStackTrace"] = haxe_NativeStackTrace


class haxe__Rest_Rest_Impl_:
    _hx_class_name = "haxe._Rest.Rest_Impl_"
    __slots__ = ()
    _hx_statics = ["get_length", "of", "_new", "get", "toArray", "iterator", "keyValueIterator", "append", "prepend", "toString"]
    length = None

    @staticmethod
    def get_length(this1):
        return len(this1)

    @staticmethod
    def of(array):
        this1 = array
        return this1

    @staticmethod
    def _new(array):
        this1 = array
        return this1

    @staticmethod
    def get(this1,index):
        return (this1[index] if index >= 0 and index < len(this1) else None)

    @staticmethod
    def toArray(this1):
        return list(this1)

    @staticmethod
    def iterator(this1):
        return haxe_iterators_RestIterator(this1)

    @staticmethod
    def keyValueIterator(this1):
        return haxe_iterators_RestKeyValueIterator(this1)

    @staticmethod
    def append(this1,item):
        result = list(this1)
        result.append(item)
        this1 = result
        return this1

    @staticmethod
    def prepend(this1,item):
        result = list(this1)
        result.insert(0, item)
        this1 = result
        return this1

    @staticmethod
    def toString(this1):
        return (("[" + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in this1]))) + "]")
haxe__Rest_Rest_Impl_._hx_class = haxe__Rest_Rest_Impl_
_hx_classes["haxe._Rest.Rest_Impl_"] = haxe__Rest_Rest_Impl_


class haxe_ValueException(haxe_Exception):
    _hx_class_name = "haxe.ValueException"
    __slots__ = ("value",)
    _hx_fields = ["value"]
    _hx_methods = ["unwrap"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_Exception


    def __init__(self,value,previous = None,native = None):
        self.value = None
        super().__init__(Std.string(value),previous,native)
        self.value = value
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0._hx___skipStack
        _hx_local_0._hx___skipStack = (_hx_local_1 + 1)
        _hx_local_1

    def unwrap(self):
        return self.value

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.value = None
haxe_ValueException._hx_class = haxe_ValueException
_hx_classes["haxe.ValueException"] = haxe_ValueException


class haxe_ds_BalancedTree:
    _hx_class_name = "haxe.ds.BalancedTree"
    __slots__ = ("root",)
    _hx_fields = ["root"]
    _hx_methods = ["set", "get", "remove", "exists", "iterator", "keyValueIterator", "keys", "copy", "setLoop", "removeLoop", "keysLoop", "merge", "minBinding", "removeMinBinding", "balance", "compare", "toString", "clear"]
    _hx_statics = ["iteratorLoop"]
    _hx_interfaces = [haxe_IMap]

    def __init__(self):
        self.root = None

    def set(self,key,value):
        self.root = self.setLoop(key,value,self.root)

    def get(self,key):
        node = self.root
        while (node is not None):
            c = self.compare(key,node.key)
            if (c == 0):
                return node.value
            if (c < 0):
                node = node.left
            else:
                node = node.right
        return None

    def remove(self,key):
        try:
            self.root = self.removeLoop(key,self.root)
            return True
        except BaseException as _g:
            None
            if Std.isOfType(haxe_Exception.caught(_g).unwrap(),str):
                return False
            else:
                raise _g

    def exists(self,key):
        node = self.root
        while (node is not None):
            c = self.compare(key,node.key)
            if (c == 0):
                return True
            elif (c < 0):
                node = node.left
            else:
                node = node.right
        return False

    def iterator(self):
        ret = []
        haxe_ds_BalancedTree.iteratorLoop(self.root,ret)
        return haxe_iterators_ArrayIterator(ret)

    def keyValueIterator(self):
        return haxe_iterators_MapKeyValueIterator(self)

    def keys(self):
        ret = []
        self.keysLoop(self.root,ret)
        return haxe_iterators_ArrayIterator(ret)

    def copy(self):
        copied = haxe_ds_BalancedTree()
        copied.root = self.root
        return copied

    def setLoop(self,k,v,node):
        if (node is None):
            return haxe_ds_TreeNode(None,k,v,None)
        c = self.compare(k,node.key)
        if (c == 0):
            return haxe_ds_TreeNode(node.left,k,v,node.right,(0 if ((node is None)) else node._height))
        elif (c < 0):
            nl = self.setLoop(k,v,node.left)
            return self.balance(nl,node.key,node.value,node.right)
        else:
            nr = self.setLoop(k,v,node.right)
            return self.balance(node.left,node.key,node.value,nr)

    def removeLoop(self,k,node):
        if (node is None):
            raise haxe_Exception.thrown("Not_found")
        c = self.compare(k,node.key)
        if (c == 0):
            return self.merge(node.left,node.right)
        elif (c < 0):
            return self.balance(self.removeLoop(k,node.left),node.key,node.value,node.right)
        else:
            return self.balance(node.left,node.key,node.value,self.removeLoop(k,node.right))

    def keysLoop(self,node,acc):
        if (node is not None):
            self.keysLoop(node.left,acc)
            x = node.key
            acc.append(x)
            self.keysLoop(node.right,acc)

    def merge(self,t1,t2):
        if (t1 is None):
            return t2
        if (t2 is None):
            return t1
        t = self.minBinding(t2)
        return self.balance(t1,t.key,t.value,self.removeMinBinding(t2))

    def minBinding(self,t):
        if (t is None):
            raise haxe_Exception.thrown("Not_found")
        elif (t.left is None):
            return t
        else:
            return self.minBinding(t.left)

    def removeMinBinding(self,t):
        if (t.left is None):
            return t.right
        else:
            return self.balance(self.removeMinBinding(t.left),t.key,t.value,t.right)

    def balance(self,l,k,v,r):
        hl = (0 if ((l is None)) else l._height)
        hr = (0 if ((r is None)) else r._height)
        if (hl > ((hr + 2))):
            _this = l.left
            _this1 = l.right
            if (((0 if ((_this is None)) else _this._height)) >= ((0 if ((_this1 is None)) else _this1._height))):
                return haxe_ds_TreeNode(l.left,l.key,l.value,haxe_ds_TreeNode(l.right,k,v,r))
            else:
                return haxe_ds_TreeNode(haxe_ds_TreeNode(l.left,l.key,l.value,l.right.left),l.right.key,l.right.value,haxe_ds_TreeNode(l.right.right,k,v,r))
        elif (hr > ((hl + 2))):
            _this = r.right
            _this1 = r.left
            if (((0 if ((_this is None)) else _this._height)) > ((0 if ((_this1 is None)) else _this1._height))):
                return haxe_ds_TreeNode(haxe_ds_TreeNode(l,k,v,r.left),r.key,r.value,r.right)
            else:
                return haxe_ds_TreeNode(haxe_ds_TreeNode(l,k,v,r.left.left),r.left.key,r.left.value,haxe_ds_TreeNode(r.left.right,r.key,r.value,r.right))
        else:
            return haxe_ds_TreeNode(l,k,v,r,(((hl if ((hl > hr)) else hr)) + 1))

    def compare(self,k1,k2):
        return Reflect.compare(k1,k2)

    def toString(self):
        if (self.root is None):
            return "{}"
        else:
            return (("{" + HxOverrides.stringOrNull(self.root.toString())) + "}")

    def clear(self):
        self.root = None

    @staticmethod
    def iteratorLoop(node,acc):
        if (node is not None):
            haxe_ds_BalancedTree.iteratorLoop(node.left,acc)
            x = node.value
            acc.append(x)
            haxe_ds_BalancedTree.iteratorLoop(node.right,acc)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.root = None
haxe_ds_BalancedTree._hx_class = haxe_ds_BalancedTree
_hx_classes["haxe.ds.BalancedTree"] = haxe_ds_BalancedTree


class haxe_ds_TreeNode:
    _hx_class_name = "haxe.ds.TreeNode"
    __slots__ = ("left", "right", "key", "value", "_height")
    _hx_fields = ["left", "right", "key", "value", "_height"]
    _hx_methods = ["toString"]

    def __init__(self,l,k,v,r,h = None):
        if (h is None):
            h = -1
        self._height = None
        self.left = l
        self.key = k
        self.value = v
        self.right = r
        if (h == -1):
            tmp = None
            _this = self.left
            _this1 = self.right
            if (((0 if ((_this is None)) else _this._height)) > ((0 if ((_this1 is None)) else _this1._height))):
                _this = self.left
                tmp = (0 if ((_this is None)) else _this._height)
            else:
                _this = self.right
                tmp = (0 if ((_this is None)) else _this._height)
            self._height = (tmp + 1)
        else:
            self._height = h

    def toString(self):
        return ((HxOverrides.stringOrNull((("" if ((self.left is None)) else (HxOverrides.stringOrNull(self.left.toString()) + ", ")))) + (((("" + Std.string(self.key)) + "=") + Std.string(self.value)))) + HxOverrides.stringOrNull((("" if ((self.right is None)) else (", " + HxOverrides.stringOrNull(self.right.toString()))))))

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.left = None
        _hx_o.right = None
        _hx_o.key = None
        _hx_o.value = None
        _hx_o._height = None
haxe_ds_TreeNode._hx_class = haxe_ds_TreeNode
_hx_classes["haxe.ds.TreeNode"] = haxe_ds_TreeNode


class haxe_ds_EnumValueMap(haxe_ds_BalancedTree):
    _hx_class_name = "haxe.ds.EnumValueMap"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["compare", "compareArgs", "compareArg", "copy"]
    _hx_statics = []
    _hx_interfaces = [haxe_IMap]
    _hx_super = haxe_ds_BalancedTree


    def __init__(self):
        super().__init__()

    def compare(self,k1,k2):
        d = (k1.index - k2.index)
        if (d != 0):
            return d
        p1 = list(k1.params)
        p2 = list(k2.params)
        if ((len(p1) == 0) and ((len(p2) == 0))):
            return 0
        return self.compareArgs(p1,p2)

    def compareArgs(self,a1,a2):
        ld = (len(a1) - len(a2))
        if (ld != 0):
            return ld
        _g = 0
        _g1 = len(a1)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            d = self.compareArg((a1[i] if i >= 0 and i < len(a1) else None),(a2[i] if i >= 0 and i < len(a2) else None))
            if (d != 0):
                return d
        return 0

    def compareArg(self,v1,v2):
        if (Reflect.isEnumValue(v1) and Reflect.isEnumValue(v2)):
            return self.compare(v1,v2)
        elif (Std.isOfType(v1,list) and Std.isOfType(v2,list)):
            return self.compareArgs(v1,v2)
        else:
            return Reflect.compare(v1,v2)

    def copy(self):
        copied = haxe_ds_EnumValueMap()
        copied.root = self.root
        return copied

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
haxe_ds_EnumValueMap._hx_class = haxe_ds_EnumValueMap
_hx_classes["haxe.ds.EnumValueMap"] = haxe_ds_EnumValueMap


class haxe_ds__HashMap_HashMap_Impl_:
    _hx_class_name = "haxe.ds._HashMap.HashMap_Impl_"
    __slots__ = ()
    _hx_statics = ["_new", "set", "get", "exists", "remove", "keys", "copy", "iterator", "keyValueIterator", "clear"]

    @staticmethod
    def _new():
        this1 = haxe_ds__HashMap_HashMapData()
        return this1

    @staticmethod
    def set(this1,k,v):
        this1.keys.set(k.hashCode(),k)
        this1.values.set(k.hashCode(),v)

    @staticmethod
    def get(this1,k):
        _this = this1.values
        key = k.hashCode()
        return _this.h.get(key,None)

    @staticmethod
    def exists(this1,k):
        _this = this1.values
        return (k.hashCode() in _this.h)

    @staticmethod
    def remove(this1,k):
        this1.values.remove(k.hashCode())
        return this1.keys.remove(k.hashCode())

    @staticmethod
    def keys(this1):
        return this1.keys.iterator()

    @staticmethod
    def copy(this1):
        copied = haxe_ds__HashMap_HashMapData()
        copied.keys = this1.keys.copy()
        copied.values = this1.values.copy()
        return copied

    @staticmethod
    def iterator(this1):
        return this1.values.iterator()

    @staticmethod
    def keyValueIterator(this1):
        return haxe_iterators_HashMapKeyValueIterator(this1)

    @staticmethod
    def clear(this1):
        this1.keys.h.clear()
        this1.values.h.clear()
haxe_ds__HashMap_HashMap_Impl_._hx_class = haxe_ds__HashMap_HashMap_Impl_
_hx_classes["haxe.ds._HashMap.HashMap_Impl_"] = haxe_ds__HashMap_HashMap_Impl_


class haxe_ds__HashMap_HashMapData:
    _hx_class_name = "haxe.ds._HashMap.HashMapData"
    __slots__ = ("keys", "values")
    _hx_fields = ["keys", "values"]

    def __init__(self):
        self.keys = haxe_ds_IntMap()
        self.values = haxe_ds_IntMap()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.keys = None
        _hx_o.values = None
haxe_ds__HashMap_HashMapData._hx_class = haxe_ds__HashMap_HashMapData
_hx_classes["haxe.ds._HashMap.HashMapData"] = haxe_ds__HashMap_HashMapData


class haxe_ds_IntMap:
    _hx_class_name = "haxe.ds.IntMap"
    __slots__ = ("h",)
    _hx_fields = ["h"]
    _hx_methods = ["set", "get", "exists", "remove", "keys", "iterator", "keyValueIterator", "copy", "toString", "clear"]
    _hx_interfaces = [haxe_IMap]

    def __init__(self):
        self.h = dict()

    def set(self,key,value):
        self.h[key] = value

    def get(self,key):
        return self.h.get(key,None)

    def exists(self,key):
        return (key in self.h)

    def remove(self,key):
        if (not (key in self.h)):
            return False
        del self.h[key]
        return True

    def keys(self):
        return python_HaxeIterator(iter(self.h.keys()))

    def iterator(self):
        return python_HaxeIterator(iter(self.h.values()))

    def keyValueIterator(self):
        return haxe_iterators_MapKeyValueIterator(self)

    def copy(self):
        copied = haxe_ds_IntMap()
        key = self.keys()
        while key.hasNext():
            key1 = key.next()
            copied.set(key1,self.h.get(key1,None))
        return copied

    def toString(self):
        s_b = python_lib_io_StringIO()
        s_b.write("{")
        it = self.keys()
        i = it
        while i.hasNext():
            i1 = i.next()
            s_b.write(Std.string(i1))
            s_b.write(" => ")
            s_b.write(Std.string(Std.string(self.h.get(i1,None))))
            if it.hasNext():
                s_b.write(", ")
        s_b.write("}")
        return s_b.getvalue()

    def clear(self):
        self.h.clear()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.h = None
haxe_ds_IntMap._hx_class = haxe_ds_IntMap
_hx_classes["haxe.ds.IntMap"] = haxe_ds_IntMap


class haxe_ds_List:
    _hx_class_name = "haxe.ds.List"
    __slots__ = ("h", "q", "length")
    _hx_fields = ["h", "q", "length"]
    _hx_methods = ["add", "push", "first", "last", "pop", "isEmpty", "clear", "remove", "iterator", "keyValueIterator", "toString", "join", "filter", "map"]

    def __init__(self):
        self.q = None
        self.h = None
        self.length = 0

    def add(self,item):
        x = haxe_ds__List_ListNode(item,None)
        if (self.h is None):
            self.h = x
        else:
            self.q.next = x
        self.q = x
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.length
        _hx_local_0.length = (_hx_local_1 + 1)
        _hx_local_1

    def push(self,item):
        x = haxe_ds__List_ListNode(item,self.h)
        self.h = x
        if (self.q is None):
            self.q = x
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.length
        _hx_local_0.length = (_hx_local_1 + 1)
        _hx_local_1

    def first(self):
        if (self.h is None):
            return None
        else:
            return self.h.item

    def last(self):
        if (self.q is None):
            return None
        else:
            return self.q.item

    def pop(self):
        if (self.h is None):
            return None
        x = self.h.item
        self.h = self.h.next
        if (self.h is None):
            self.q = None
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.length
        _hx_local_0.length = (_hx_local_1 - 1)
        _hx_local_1
        return x

    def isEmpty(self):
        return (self.h is None)

    def clear(self):
        self.h = None
        self.q = None
        self.length = 0

    def remove(self,v):
        prev = None
        l = self.h
        while (l is not None):
            if HxOverrides.eq(l.item,v):
                if (prev is None):
                    self.h = l.next
                else:
                    prev.next = l.next
                if (self.q == l):
                    self.q = prev
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.length
                _hx_local_0.length = (_hx_local_1 - 1)
                _hx_local_1
                return True
            prev = l
            l = l.next
        return False

    def iterator(self):
        return haxe_ds__List_ListIterator(self.h)

    def keyValueIterator(self):
        return haxe_ds__List_ListKeyValueIterator(self.h)

    def toString(self):
        s_b = python_lib_io_StringIO()
        first = True
        l = self.h
        s_b.write("{")
        while (l is not None):
            if first:
                first = False
            else:
                s_b.write(", ")
            s_b.write(Std.string(Std.string(l.item)))
            l = l.next
        s_b.write("}")
        return s_b.getvalue()

    def join(self,sep):
        s_b = python_lib_io_StringIO()
        first = True
        l = self.h
        while (l is not None):
            if first:
                first = False
            else:
                s_b.write(Std.string(sep))
            s_b.write(Std.string(l.item))
            l = l.next
        return s_b.getvalue()

    def filter(self,f):
        l2 = haxe_ds_List()
        l = self.h
        while (l is not None):
            v = l.item
            l = l.next
            if f(v):
                l2.add(v)
        return l2

    def map(self,f):
        b = haxe_ds_List()
        l = self.h
        while (l is not None):
            v = l.item
            l = l.next
            b.add(f(v))
        return b

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.h = None
        _hx_o.q = None
        _hx_o.length = None
haxe_ds_List._hx_class = haxe_ds_List
_hx_classes["haxe.ds.List"] = haxe_ds_List


class haxe_ds__List_ListNode:
    _hx_class_name = "haxe.ds._List.ListNode"
    __slots__ = ("item", "next")
    _hx_fields = ["item", "next"]

    def __init__(self,item,next):
        self.item = item
        self.next = next

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.item = None
        _hx_o.next = None
haxe_ds__List_ListNode._hx_class = haxe_ds__List_ListNode
_hx_classes["haxe.ds._List.ListNode"] = haxe_ds__List_ListNode


class haxe_ds__List_ListIterator:
    _hx_class_name = "haxe.ds._List.ListIterator"
    __slots__ = ("head",)
    _hx_fields = ["head"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,head):
        self.head = head

    def hasNext(self):
        return (self.head is not None)

    def next(self):
        val = self.head.item
        self.head = self.head.next
        return val

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.head = None
haxe_ds__List_ListIterator._hx_class = haxe_ds__List_ListIterator
_hx_classes["haxe.ds._List.ListIterator"] = haxe_ds__List_ListIterator


class haxe_ds__List_ListKeyValueIterator:
    _hx_class_name = "haxe.ds._List.ListKeyValueIterator"
    __slots__ = ("idx", "head")
    _hx_fields = ["idx", "head"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,head):
        self.head = head
        self.idx = 0

    def hasNext(self):
        return (self.head is not None)

    def next(self):
        val = self.head.item
        self.head = self.head.next
        def _hx_local_3():
            def _hx_local_2():
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.idx
                _hx_local_0.idx = (_hx_local_1 + 1)
                return _hx_local_1
            return _hx_AnonObject({'value': val, 'key': _hx_local_2()})
        return _hx_local_3()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.idx = None
        _hx_o.head = None
haxe_ds__List_ListKeyValueIterator._hx_class = haxe_ds__List_ListKeyValueIterator
_hx_classes["haxe.ds._List.ListKeyValueIterator"] = haxe_ds__List_ListKeyValueIterator


class haxe_ds__Map_Map_Impl_:
    _hx_class_name = "haxe.ds._Map.Map_Impl_"
    __slots__ = ()
    _hx_statics = ["set", "get", "exists", "remove", "keys", "iterator", "keyValueIterator", "copy", "toString", "clear", "arrayWrite", "toStringMap", "toIntMap", "toEnumValueMapMap", "toObjectMap", "fromStringMap", "fromIntMap", "fromObjectMap"]

    @staticmethod
    def set(this1,key,value):
        this1.set(key,value)

    @staticmethod
    def get(this1,key):
        return this1.get(key)

    @staticmethod
    def exists(this1,key):
        return this1.exists(key)

    @staticmethod
    def remove(this1,key):
        return this1.remove(key)

    @staticmethod
    def keys(this1):
        return this1.keys()

    @staticmethod
    def iterator(this1):
        return this1.iterator()

    @staticmethod
    def keyValueIterator(this1):
        return this1.keyValueIterator()

    @staticmethod
    def copy(this1):
        return this1.copy()

    @staticmethod
    def toString(this1):
        return this1.toString()

    @staticmethod
    def clear(this1):
        this1.clear()

    @staticmethod
    def arrayWrite(this1,k,v):
        this1.set(k,v)
        return v

    @staticmethod
    def toStringMap(t):
        return haxe_ds_StringMap()

    @staticmethod
    def toIntMap(t):
        return haxe_ds_IntMap()

    @staticmethod
    def toEnumValueMapMap(t):
        return haxe_ds_EnumValueMap()

    @staticmethod
    def toObjectMap(t):
        return haxe_ds_ObjectMap()

    @staticmethod
    def fromStringMap(_hx_map):
        return _hx_map

    @staticmethod
    def fromIntMap(_hx_map):
        return _hx_map

    @staticmethod
    def fromObjectMap(_hx_map):
        return _hx_map
haxe_ds__Map_Map_Impl_._hx_class = haxe_ds__Map_Map_Impl_
_hx_classes["haxe.ds._Map.Map_Impl_"] = haxe_ds__Map_Map_Impl_


class haxe_ds_ObjectMap:
    _hx_class_name = "haxe.ds.ObjectMap"
    __slots__ = ("h",)
    _hx_fields = ["h"]
    _hx_methods = ["set", "get", "exists", "remove", "keys", "iterator", "keyValueIterator", "copy", "toString", "clear"]
    _hx_interfaces = [haxe_IMap]

    def __init__(self):
        self.h = dict()

    def set(self,key,value):
        self.h[key] = value

    def get(self,key):
        return self.h.get(key,None)

    def exists(self,key):
        return (key in self.h)

    def remove(self,key):
        r = (key in self.h)
        if r:
            del self.h[key]
        return r

    def keys(self):
        return python_HaxeIterator(iter(self.h.keys()))

    def iterator(self):
        return python_HaxeIterator(iter(self.h.values()))

    def keyValueIterator(self):
        return haxe_iterators_MapKeyValueIterator(self)

    def copy(self):
        copied = haxe_ds_ObjectMap()
        key = self.keys()
        while key.hasNext():
            key1 = key.next()
            copied.set(key1,self.h.get(key1,None))
        return copied

    def toString(self):
        s_b = python_lib_io_StringIO()
        s_b.write("{")
        it = self.keys()
        i = it
        while i.hasNext():
            i1 = i.next()
            s_b.write(Std.string(Std.string(i1)))
            s_b.write(" => ")
            s_b.write(Std.string(Std.string(self.h.get(i1,None))))
            if it.hasNext():
                s_b.write(", ")
        s_b.write("}")
        return s_b.getvalue()

    def clear(self):
        self.h.clear()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.h = None
haxe_ds_ObjectMap._hx_class = haxe_ds_ObjectMap
_hx_classes["haxe.ds.ObjectMap"] = haxe_ds_ObjectMap

class haxe_ds_Option(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.ds.Option"
    _hx_constructs = ["Some", "None"]

    @staticmethod
    def Some(v):
        return haxe_ds_Option("Some", 0, (v,))
haxe_ds_Option._hx_None = haxe_ds_Option("None", 1, ())
haxe_ds_Option._hx_class = haxe_ds_Option
_hx_classes["haxe.ds.Option"] = haxe_ds_Option


class haxe_ds__ReadOnlyArray_ReadOnlyArray_Impl_:
    _hx_class_name = "haxe.ds._ReadOnlyArray.ReadOnlyArray_Impl_"
    __slots__ = ()
    _hx_statics = ["get_length", "get", "concat"]
    length = None

    @staticmethod
    def get_length(this1):
        return len(this1)

    @staticmethod
    def get(this1,i):
        return (this1[i] if i >= 0 and i < len(this1) else None)

    @staticmethod
    def concat(this1,a):
        return (this1 + a)
haxe_ds__ReadOnlyArray_ReadOnlyArray_Impl_._hx_class = haxe_ds__ReadOnlyArray_ReadOnlyArray_Impl_
_hx_classes["haxe.ds._ReadOnlyArray.ReadOnlyArray_Impl_"] = haxe_ds__ReadOnlyArray_ReadOnlyArray_Impl_


class haxe_ds_StringMap:
    _hx_class_name = "haxe.ds.StringMap"
    __slots__ = ("h",)
    _hx_fields = ["h"]
    _hx_methods = ["set", "get", "exists", "remove", "keys", "iterator", "keyValueIterator", "copy", "toString", "clear"]
    _hx_interfaces = [haxe_IMap]

    def __init__(self):
        self.h = dict()

    def set(self,key,value):
        self.h[key] = value

    def get(self,key):
        return self.h.get(key,None)

    def exists(self,key):
        return (key in self.h)

    def remove(self,key):
        has = (key in self.h)
        if has:
            del self.h[key]
        return has

    def keys(self):
        return python_HaxeIterator(iter(self.h.keys()))

    def iterator(self):
        return python_HaxeIterator(iter(self.h.values()))

    def keyValueIterator(self):
        return haxe_iterators_MapKeyValueIterator(self)

    def copy(self):
        copied = haxe_ds_StringMap()
        key = self.keys()
        while key.hasNext():
            key1 = key.next()
            value = self.h.get(key1,None)
            copied.h[key1] = value
        return copied

    def toString(self):
        s_b = python_lib_io_StringIO()
        s_b.write("{")
        it = self.keys()
        i = it
        while i.hasNext():
            i1 = i.next()
            s_b.write(Std.string(i1))
            s_b.write(" => ")
            s_b.write(Std.string(Std.string(self.h.get(i1,None))))
            if it.hasNext():
                s_b.write(", ")
        s_b.write("}")
        return s_b.getvalue()

    def clear(self):
        self.h.clear()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.h = None
haxe_ds_StringMap._hx_class = haxe_ds_StringMap
_hx_classes["haxe.ds.StringMap"] = haxe_ds_StringMap


class haxe_ds_WeakMap:
    _hx_class_name = "haxe.ds.WeakMap"
    __slots__ = ()
    _hx_methods = ["set", "get", "exists", "remove", "keys", "iterator", "keyValueIterator", "copy", "toString", "clear"]
    _hx_interfaces = [haxe_IMap]

    def __init__(self):
        raise haxe_exceptions_NotImplementedException("Not implemented for this platform",None,_hx_AnonObject({'fileName': "haxe/ds/WeakMap.hx", 'lineNumber': 39, 'className': "haxe.ds.WeakMap", 'methodName': "new"}))

    def set(self,key,value):
        pass

    def get(self,key):
        return None

    def exists(self,key):
        return False

    def remove(self,key):
        return False

    def keys(self):
        return None

    def iterator(self):
        return None

    def keyValueIterator(self):
        return None

    def copy(self):
        return None

    def toString(self):
        return None

    def clear(self):
        pass

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
haxe_ds_WeakMap._hx_class = haxe_ds_WeakMap
_hx_classes["haxe.ds.WeakMap"] = haxe_ds_WeakMap


class haxe_exceptions_PosException(haxe_Exception):
    _hx_class_name = "haxe.exceptions.PosException"
    __slots__ = ("posInfos",)
    _hx_fields = ["posInfos"]
    _hx_methods = ["toString"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_Exception


    def __init__(self,message,previous = None,pos = None):
        self.posInfos = None
        super().__init__(message,previous)
        if (pos is None):
            self.posInfos = _hx_AnonObject({'fileName': "(unknown)", 'lineNumber': 0, 'className': "(unknown)", 'methodName': "(unknown)"})
        else:
            self.posInfos = pos
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0._hx___skipStack
        _hx_local_0._hx___skipStack = (_hx_local_1 + 1)
        _hx_local_1

    def toString(self):
        return ((((((((("" + HxOverrides.stringOrNull(super().toString())) + " in ") + HxOverrides.stringOrNull(self.posInfos.className)) + ".") + HxOverrides.stringOrNull(self.posInfos.methodName)) + " at ") + HxOverrides.stringOrNull(self.posInfos.fileName)) + ":") + Std.string(self.posInfos.lineNumber))

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.posInfos = None
haxe_exceptions_PosException._hx_class = haxe_exceptions_PosException
_hx_classes["haxe.exceptions.PosException"] = haxe_exceptions_PosException


class haxe_exceptions_NotImplementedException(haxe_exceptions_PosException):
    _hx_class_name = "haxe.exceptions.NotImplementedException"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_exceptions_PosException


    def __init__(self,message = None,previous = None,pos = None):
        if (message is None):
            message = "Not implemented"
        super().__init__(message,previous,pos)
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0._hx___skipStack
        _hx_local_0._hx___skipStack = (_hx_local_1 + 1)
        _hx_local_1
haxe_exceptions_NotImplementedException._hx_class = haxe_exceptions_NotImplementedException
_hx_classes["haxe.exceptions.NotImplementedException"] = haxe_exceptions_NotImplementedException


class haxe_format_JsonPrinter:
    _hx_class_name = "haxe.format.JsonPrinter"
    __slots__ = ("buf", "replacer", "indent", "pretty", "nind")
    _hx_fields = ["buf", "replacer", "indent", "pretty", "nind"]
    _hx_methods = ["ipad", "newl", "write", "classString", "objString", "fieldsString", "quote"]
    _hx_statics = ["print"]

    def __init__(self,replacer,space):
        self.replacer = replacer
        self.indent = space
        self.pretty = (space is not None)
        self.nind = 0
        self.buf = StringBuf()

    def ipad(self):
        if self.pretty:
            v = StringTools.lpad("",self.indent,(self.nind * len(self.indent)))
            _this = self.buf
            s = Std.string(v)
            _this.b.write(s)

    def newl(self):
        if self.pretty:
            _this = self.buf
            s = "".join(map(chr,[10]))
            _this.b.write(s)

    def write(self,k,v):
        if (self.replacer is not None):
            v = self.replacer(k,v)
        _g = Type.typeof(v)
        tmp = _g.index
        if (tmp == 0):
            self.buf.b.write("null")
        elif (tmp == 1):
            _this = self.buf
            s = Std.string(v)
            _this.b.write(s)
        elif (tmp == 2):
            f = v
            v1 = (Std.string(v) if ((((f != Math.POSITIVE_INFINITY) and ((f != Math.NEGATIVE_INFINITY))) and (not python_lib_Math.isnan(f)))) else "null")
            _this = self.buf
            s = Std.string(v1)
            _this.b.write(s)
        elif (tmp == 3):
            _this = self.buf
            s = Std.string(v)
            _this.b.write(s)
        elif (tmp == 4):
            self.fieldsString(v,python_Boot.fields(v))
        elif (tmp == 5):
            self.buf.b.write("\"<fun>\"")
        elif (tmp == 6):
            c = _g.params[0]
            if (c == str):
                self.quote(v)
            elif (c == list):
                v1 = v
                _this = self.buf
                s = "".join(map(chr,[91]))
                _this.b.write(s)
                _hx_len = len(v1)
                last = (_hx_len - 1)
                _g1 = 0
                _g2 = _hx_len
                while (_g1 < _g2):
                    i = _g1
                    _g1 = (_g1 + 1)
                    if (i > 0):
                        _this = self.buf
                        s = "".join(map(chr,[44]))
                        _this.b.write(s)
                    else:
                        _hx_local_0 = self
                        _hx_local_1 = _hx_local_0.nind
                        _hx_local_0.nind = (_hx_local_1 + 1)
                        _hx_local_1
                    if self.pretty:
                        _this1 = self.buf
                        s1 = "".join(map(chr,[10]))
                        _this1.b.write(s1)
                    if self.pretty:
                        v2 = StringTools.lpad("",self.indent,(self.nind * len(self.indent)))
                        _this2 = self.buf
                        s2 = Std.string(v2)
                        _this2.b.write(s2)
                    self.write(i,(v1[i] if i >= 0 and i < len(v1) else None))
                    if (i == last):
                        _hx_local_2 = self
                        _hx_local_3 = _hx_local_2.nind
                        _hx_local_2.nind = (_hx_local_3 - 1)
                        _hx_local_3
                        if self.pretty:
                            _this3 = self.buf
                            s3 = "".join(map(chr,[10]))
                            _this3.b.write(s3)
                        if self.pretty:
                            v3 = StringTools.lpad("",self.indent,(self.nind * len(self.indent)))
                            _this4 = self.buf
                            s4 = Std.string(v3)
                            _this4.b.write(s4)
                _this = self.buf
                s = "".join(map(chr,[93]))
                _this.b.write(s)
            elif (c == haxe_ds_StringMap):
                v1 = v
                o = _hx_AnonObject({})
                k = v1.keys()
                while k.hasNext():
                    k1 = k.next()
                    value = v1.h.get(k1,None)
                    setattr(o,(("_hx_" + k1) if ((k1 in python_Boot.keywords)) else (("_hx_" + k1) if (((((len(k1) > 2) and ((ord(k1[0]) == 95))) and ((ord(k1[1]) == 95))) and ((ord(k1[(len(k1) - 1)]) != 95)))) else k1)),value)
                v1 = o
                self.fieldsString(v1,python_Boot.fields(v1))
            elif (c == Date):
                v1 = v
                self.quote(v1.toString())
            else:
                self.classString(v)
        elif (tmp == 7):
            _g1 = _g.params[0]
            i = v.index
            _this = self.buf
            s = Std.string(i)
            _this.b.write(s)
        elif (tmp == 8):
            self.buf.b.write("\"???\"")
        else:
            pass

    def classString(self,v):
        self.fieldsString(v,python_Boot.getInstanceFields(Type.getClass(v)))

    def objString(self,v):
        self.fieldsString(v,python_Boot.fields(v))

    def fieldsString(self,v,fields):
        _this = self.buf
        s = "".join(map(chr,[123]))
        _this.b.write(s)
        _hx_len = len(fields)
        last = (_hx_len - 1)
        first = True
        _g = 0
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            f = (fields[i] if i >= 0 and i < len(fields) else None)
            value = Reflect.field(v,f)
            if Reflect.isFunction(value):
                continue
            if first:
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.nind
                _hx_local_0.nind = (_hx_local_1 + 1)
                _hx_local_1
                first = False
            else:
                _this = self.buf
                s = "".join(map(chr,[44]))
                _this.b.write(s)
            if self.pretty:
                _this1 = self.buf
                s1 = "".join(map(chr,[10]))
                _this1.b.write(s1)
            if self.pretty:
                v1 = StringTools.lpad("",self.indent,(self.nind * len(self.indent)))
                _this2 = self.buf
                s2 = Std.string(v1)
                _this2.b.write(s2)
            self.quote(f)
            _this3 = self.buf
            s3 = "".join(map(chr,[58]))
            _this3.b.write(s3)
            if self.pretty:
                _this4 = self.buf
                s4 = "".join(map(chr,[32]))
                _this4.b.write(s4)
            self.write(f,value)
            if (i == last):
                _hx_local_2 = self
                _hx_local_3 = _hx_local_2.nind
                _hx_local_2.nind = (_hx_local_3 - 1)
                _hx_local_3
                if self.pretty:
                    _this5 = self.buf
                    s5 = "".join(map(chr,[10]))
                    _this5.b.write(s5)
                if self.pretty:
                    v2 = StringTools.lpad("",self.indent,(self.nind * len(self.indent)))
                    _this6 = self.buf
                    s6 = Std.string(v2)
                    _this6.b.write(s6)
        _this = self.buf
        s = "".join(map(chr,[125]))
        _this.b.write(s)

    def quote(self,s):
        _this = self.buf
        s1 = "".join(map(chr,[34]))
        _this.b.write(s1)
        i = 0
        length = len(s)
        while (i < length):
            index = i
            i = (i + 1)
            c = ord(s[index])
            c1 = c
            if (c1 == 8):
                self.buf.b.write("\\b")
            elif (c1 == 9):
                self.buf.b.write("\\t")
            elif (c1 == 10):
                self.buf.b.write("\\n")
            elif (c1 == 12):
                self.buf.b.write("\\f")
            elif (c1 == 13):
                self.buf.b.write("\\r")
            elif (c1 == 34):
                self.buf.b.write("\\\"")
            elif (c1 == 92):
                self.buf.b.write("\\\\")
            else:
                _this = self.buf
                s1 = "".join(map(chr,[c]))
                _this.b.write(s1)
        _this = self.buf
        s = "".join(map(chr,[34]))
        _this.b.write(s)

    @staticmethod
    def print(o,replacer = None,space = None):
        printer = haxe_format_JsonPrinter(replacer,space)
        printer.write("",o)
        return printer.buf.b.getvalue()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.buf = None
        _hx_o.replacer = None
        _hx_o.indent = None
        _hx_o.pretty = None
        _hx_o.nind = None
haxe_format_JsonPrinter._hx_class = haxe_format_JsonPrinter
_hx_classes["haxe.format.JsonPrinter"] = haxe_format_JsonPrinter


class haxe_io_Bytes:
    _hx_class_name = "haxe.io.Bytes"
    __slots__ = ("length", "b")
    _hx_fields = ["length", "b"]
    _hx_methods = ["get", "set", "blit", "fill", "sub", "compare", "getDouble", "getFloat", "setDouble", "setFloat", "getUInt16", "setUInt16", "getInt32", "getInt64", "setInt32", "setInt64", "getString", "readString", "toString", "toHex", "getData"]
    _hx_statics = ["alloc", "ofString", "ofData", "ofHex", "fastGet"]

    def __init__(self,length,b):
        self.length = length
        self.b = b

    def get(self,pos):
        return self.b[pos]

    def set(self,pos,v):
        self.b[pos] = (v & 255)

    def blit(self,pos,src,srcpos,_hx_len):
        if (((((pos < 0) or ((srcpos < 0))) or ((_hx_len < 0))) or (((pos + _hx_len) > self.length))) or (((srcpos + _hx_len) > src.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        self.b[pos:pos+_hx_len] = src.b[srcpos:srcpos+_hx_len]

    def fill(self,pos,_hx_len,value):
        _g = 0
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            pos1 = pos
            pos = (pos + 1)
            self.b[pos1] = (value & 255)

    def sub(self,pos,_hx_len):
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > self.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        return haxe_io_Bytes(_hx_len,self.b[pos:(pos + _hx_len)])

    def compare(self,other):
        b1 = self.b
        b2 = other.b
        _hx_len = (self.length if ((self.length < other.length)) else other.length)
        _g = 0
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (b1[i] != b2[i]):
                return (b1[i] - b2[i])
        return (self.length - other.length)

    def getDouble(self,pos):
        v = (((self.b[pos] | ((self.b[(pos + 1)] << 8))) | ((self.b[(pos + 2)] << 16))) | ((self.b[(pos + 3)] << 24)))
        pos1 = (pos + 4)
        v1 = (((self.b[pos1] | ((self.b[(pos1 + 1)] << 8))) | ((self.b[(pos1 + 2)] << 16))) | ((self.b[(pos1 + 3)] << 24)))
        return haxe_io_FPHelper.i64ToDouble(((v | -2147483648) if ((((v & -2147483648)) != 0)) else v),((v1 | -2147483648) if ((((v1 & -2147483648)) != 0)) else v1))

    def getFloat(self,pos):
        v = (((self.b[pos] | ((self.b[(pos + 1)] << 8))) | ((self.b[(pos + 2)] << 16))) | ((self.b[(pos + 3)] << 24)))
        return haxe_io_FPHelper.i32ToFloat(((v | -2147483648) if ((((v & -2147483648)) != 0)) else v))

    def setDouble(self,pos,v):
        i = haxe_io_FPHelper.doubleToI64(v)
        v = i.low
        self.b[pos] = (v & 255)
        self.b[(pos + 1)] = ((v >> 8) & 255)
        self.b[(pos + 2)] = ((v >> 16) & 255)
        self.b[(pos + 3)] = (HxOverrides.rshift(v, 24) & 255)
        pos1 = (pos + 4)
        v = i.high
        self.b[pos1] = (v & 255)
        self.b[(pos1 + 1)] = ((v >> 8) & 255)
        self.b[(pos1 + 2)] = ((v >> 16) & 255)
        self.b[(pos1 + 3)] = (HxOverrides.rshift(v, 24) & 255)

    def setFloat(self,pos,v):
        v1 = haxe_io_FPHelper.floatToI32(v)
        self.b[pos] = (v1 & 255)
        self.b[(pos + 1)] = ((v1 >> 8) & 255)
        self.b[(pos + 2)] = ((v1 >> 16) & 255)
        self.b[(pos + 3)] = (HxOverrides.rshift(v1, 24) & 255)

    def getUInt16(self,pos):
        return (self.b[pos] | ((self.b[(pos + 1)] << 8)))

    def setUInt16(self,pos,v):
        self.b[pos] = (v & 255)
        self.b[(pos + 1)] = ((v >> 8) & 255)

    def getInt32(self,pos):
        v = (((self.b[pos] | ((self.b[(pos + 1)] << 8))) | ((self.b[(pos + 2)] << 16))) | ((self.b[(pos + 3)] << 24)))
        if (((v & -2147483648)) != 0):
            return (v | -2147483648)
        else:
            return v

    def getInt64(self,pos):
        pos1 = (pos + 4)
        v = (((self.b[pos1] | ((self.b[(pos1 + 1)] << 8))) | ((self.b[(pos1 + 2)] << 16))) | ((self.b[(pos1 + 3)] << 24)))
        v1 = (((self.b[pos] | ((self.b[(pos + 1)] << 8))) | ((self.b[(pos + 2)] << 16))) | ((self.b[(pos + 3)] << 24)))
        this1 = haxe__Int64____Int64(((v | -2147483648) if ((((v & -2147483648)) != 0)) else v),((v1 | -2147483648) if ((((v1 & -2147483648)) != 0)) else v1))
        return this1

    def setInt32(self,pos,v):
        self.b[pos] = (v & 255)
        self.b[(pos + 1)] = ((v >> 8) & 255)
        self.b[(pos + 2)] = ((v >> 16) & 255)
        self.b[(pos + 3)] = (HxOverrides.rshift(v, 24) & 255)

    def setInt64(self,pos,v):
        v1 = v.low
        self.b[pos] = (v1 & 255)
        self.b[(pos + 1)] = ((v1 >> 8) & 255)
        self.b[(pos + 2)] = ((v1 >> 16) & 255)
        self.b[(pos + 3)] = (HxOverrides.rshift(v1, 24) & 255)
        pos1 = (pos + 4)
        v1 = v.high
        self.b[pos1] = (v1 & 255)
        self.b[(pos1 + 1)] = ((v1 >> 8) & 255)
        self.b[(pos1 + 2)] = ((v1 >> 16) & 255)
        self.b[(pos1 + 3)] = (HxOverrides.rshift(v1, 24) & 255)

    def getString(self,pos,_hx_len,encoding = None):
        tmp = (encoding is None)
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > self.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        return self.b[pos:pos+_hx_len].decode('UTF-8','replace')

    def readString(self,pos,_hx_len):
        return self.getString(pos,_hx_len)

    def toString(self):
        return self.getString(0,self.length)

    def toHex(self):
        s_b = python_lib_io_StringIO()
        chars = []
        _hx_str = "0123456789abcdef"
        _g = 0
        _g1 = len(_hx_str)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            x = HxString.charCodeAt(_hx_str,i)
            chars.append(x)
        _g = 0
        _g1 = self.length
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            c = self.b[i]
            s_b.write("".join(map(chr,[python_internal_ArrayImpl._get(chars, (c >> 4))])))
            s_b.write("".join(map(chr,[python_internal_ArrayImpl._get(chars, (c & 15))])))
        return s_b.getvalue()

    def getData(self):
        return self.b

    @staticmethod
    def alloc(length):
        return haxe_io_Bytes(length,bytearray(length))

    @staticmethod
    def ofString(s,encoding = None):
        b = bytearray(s,"UTF-8")
        return haxe_io_Bytes(len(b),b)

    @staticmethod
    def ofData(b):
        return haxe_io_Bytes(len(b),b)

    @staticmethod
    def ofHex(s):
        _hx_len = len(s)
        if (((_hx_len & 1)) != 0):
            raise haxe_Exception.thrown("Not a hex string (odd number of digits)")
        ret = haxe_io_Bytes.alloc((_hx_len >> 1))
        _g = 0
        _g1 = ret.length
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            index = (i * 2)
            high = (-1 if ((index >= len(s))) else ord(s[index]))
            index1 = ((i * 2) + 1)
            low = (-1 if ((index1 >= len(s))) else ord(s[index1]))
            high = (((high & 15)) + ((((((high & 64)) >> 6)) * 9)))
            low = (((low & 15)) + ((((((low & 64)) >> 6)) * 9)))
            ret.b[i] = (((((high << 4) | low)) & 255) & 255)
        return ret

    @staticmethod
    def fastGet(b,pos):
        return b[pos]

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.length = None
        _hx_o.b = None
haxe_io_Bytes._hx_class = haxe_io_Bytes
_hx_classes["haxe.io.Bytes"] = haxe_io_Bytes


class haxe_io_BytesBuffer:
    _hx_class_name = "haxe.io.BytesBuffer"
    __slots__ = ("b",)
    _hx_fields = ["b"]
    _hx_methods = ["get_length", "addByte", "add", "addString", "addInt32", "addInt64", "addFloat", "addDouble", "addBytes", "getBytes"]

    def __init__(self):
        self.b = bytearray()

    def get_length(self):
        return len(self.b)

    def addByte(self,byte):
        self.b.append(byte)

    def add(self,src):
        self.b.extend(src.b)

    def addString(self,v,encoding = None):
        self.b.extend(bytearray(v,"UTF-8"))

    def addInt32(self,v):
        self.b.append((v & 255))
        self.b.append(((v >> 8) & 255))
        self.b.append(((v >> 16) & 255))
        self.b.append(HxOverrides.rshift(v, 24))

    def addInt64(self,v):
        self.addInt32(v.low)
        self.addInt32(v.high)

    def addFloat(self,v):
        self.addInt32(haxe_io_FPHelper.floatToI32(v))

    def addDouble(self,v):
        self.addInt64(haxe_io_FPHelper.doubleToI64(v))

    def addBytes(self,src,pos,_hx_len):
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > src.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        self.b.extend(src.b[pos:(pos + _hx_len)])

    def getBytes(self):
        _hx_bytes = haxe_io_Bytes(len(self.b),self.b)
        self.b = None
        return _hx_bytes

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.b = None
haxe_io_BytesBuffer._hx_class = haxe_io_BytesBuffer
_hx_classes["haxe.io.BytesBuffer"] = haxe_io_BytesBuffer

class haxe_io_Encoding(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.io.Encoding"
    _hx_constructs = ["UTF8", "RawNative"]
haxe_io_Encoding.UTF8 = haxe_io_Encoding("UTF8", 0, ())
haxe_io_Encoding.RawNative = haxe_io_Encoding("RawNative", 1, ())
haxe_io_Encoding._hx_class = haxe_io_Encoding
_hx_classes["haxe.io.Encoding"] = haxe_io_Encoding


class haxe_io_Eof:
    _hx_class_name = "haxe.io.Eof"
    __slots__ = ()
    _hx_methods = ["toString"]

    def __init__(self):
        pass

    def toString(self):
        return "Eof"

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
haxe_io_Eof._hx_class = haxe_io_Eof
_hx_classes["haxe.io.Eof"] = haxe_io_Eof

class haxe_io_Error(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.io.Error"
    _hx_constructs = ["Blocked", "Overflow", "OutsideBounds", "Custom"]

    @staticmethod
    def Custom(e):
        return haxe_io_Error("Custom", 3, (e,))
haxe_io_Error.Blocked = haxe_io_Error("Blocked", 0, ())
haxe_io_Error.Overflow = haxe_io_Error("Overflow", 1, ())
haxe_io_Error.OutsideBounds = haxe_io_Error("OutsideBounds", 2, ())
haxe_io_Error._hx_class = haxe_io_Error
_hx_classes["haxe.io.Error"] = haxe_io_Error


class haxe_io_FPHelper:
    _hx_class_name = "haxe.io.FPHelper"
    __slots__ = ()
    _hx_statics = ["i64tmp", "LN2", "_i32ToFloat", "_i64ToDouble", "_floatToI32", "_doubleToI64", "i32ToFloat", "floatToI32", "i64ToDouble", "doubleToI64"]

    @staticmethod
    def _i32ToFloat(i):
        sign = (1 - ((HxOverrides.rshift(i, 31) << 1)))
        e = ((i >> 23) & 255)
        if (e == 255):
            if (((i & 8388607)) == 0):
                if (sign > 0):
                    return Math.POSITIVE_INFINITY
                else:
                    return Math.NEGATIVE_INFINITY
            else:
                return Math.NaN
        m = ((((i & 8388607)) << 1) if ((e == 0)) else ((i & 8388607) | 8388608))
        return ((sign * m) * Math.pow(2,(e - 150)))

    @staticmethod
    def _i64ToDouble(lo,hi):
        sign = (1 - ((HxOverrides.rshift(hi, 31) << 1)))
        e = ((hi >> 20) & 2047)
        if (e == 2047):
            if ((lo == 0) and ((((hi & 1048575)) == 0))):
                if (sign > 0):
                    return Math.POSITIVE_INFINITY
                else:
                    return Math.NEGATIVE_INFINITY
            else:
                return Math.NaN
        m = (2.220446049250313e-16 * ((((((hi & 1048575)) * 4294967296.) + (((HxOverrides.rshift(lo, 31)) * 2147483648.))) + ((lo & 2147483647)))))
        if (e == 0):
            m = (m * 2.0)
        else:
            m = (m + 1.0)
        return ((sign * m) * Math.pow(2,(e - 1023)))

    @staticmethod
    def _floatToI32(f):
        if (f == 0):
            return 0
        af = (-f if ((f < 0)) else f)
        exp = Math.floor((((Math.NEGATIVE_INFINITY if ((af == 0.0)) else (Math.NaN if ((af < 0.0)) else python_lib_Math.log(af)))) / 0.6931471805599453))
        if (exp > 127):
            return 2139095040
        else:
            if (exp <= -127):
                exp = -127
                af = (af * 7.1362384635298e+44)
            else:
                af = ((((af / Math.pow(2,exp)) - 1.0)) * 8388608)
            return ((((-2147483648 if ((f < 0)) else 0)) | (((exp + 127) << 23))) | Math.floor((af + 0.5)))

    @staticmethod
    def _doubleToI64(v):
        i64 = haxe_io_FPHelper.i64tmp
        if (v == 0):
            i64.low = 0
            i64.high = 0
        elif (not ((((v != Math.POSITIVE_INFINITY) and ((v != Math.NEGATIVE_INFINITY))) and (not python_lib_Math.isnan(v))))):
            i64.low = 0
            i64.high = (2146435072 if ((v > 0)) else -1048576)
        else:
            av = (-v if ((v < 0)) else v)
            exp = Math.floor((((Math.NEGATIVE_INFINITY if ((av == 0.0)) else (Math.NaN if ((av < 0.0)) else python_lib_Math.log(av)))) / 0.6931471805599453))
            if (exp > 1023):
                i64.low = -1
                i64.high = 2146435071
            else:
                if (exp <= -1023):
                    exp = -1023
                    av = (av / 2.2250738585072014e-308)
                else:
                    av = ((av / Math.pow(2,exp)) - 1.0)
                v1 = (av * 4503599627370496.)
                sig = (v1 if (((v1 == Math.POSITIVE_INFINITY) or ((v1 == Math.NEGATIVE_INFINITY)))) else (Math.NaN if (python_lib_Math.isnan(v1)) else Math.floor((v1 + 0.5))))
                sig_l = None
                try:
                    sig_l = int(sig)
                except BaseException as _g:
                    None
                    sig_l = None
                sig_l1 = sig_l
                sig_h = None
                try:
                    sig_h = int((sig / 4294967296.0))
                except BaseException as _g:
                    None
                    sig_h = None
                sig_h1 = sig_h
                i64.low = sig_l1
                i64.high = ((((-2147483648 if ((v < 0)) else 0)) | (((exp + 1023) << 20))) | sig_h1)
        return i64

    @staticmethod
    def i32ToFloat(i):
        sign = (1 - ((HxOverrides.rshift(i, 31) << 1)))
        e = ((i >> 23) & 255)
        if (e == 255):
            if (((i & 8388607)) == 0):
                if (sign > 0):
                    return Math.POSITIVE_INFINITY
                else:
                    return Math.NEGATIVE_INFINITY
            else:
                return Math.NaN
        else:
            m = ((((i & 8388607)) << 1) if ((e == 0)) else ((i & 8388607) | 8388608))
            return ((sign * m) * Math.pow(2,(e - 150)))

    @staticmethod
    def floatToI32(f):
        if (f == 0):
            return 0
        else:
            af = (-f if ((f < 0)) else f)
            exp = Math.floor((((Math.NEGATIVE_INFINITY if ((af == 0.0)) else (Math.NaN if ((af < 0.0)) else python_lib_Math.log(af)))) / 0.6931471805599453))
            if (exp > 127):
                return 2139095040
            else:
                if (exp <= -127):
                    exp = -127
                    af = (af * 7.1362384635298e+44)
                else:
                    af = ((((af / Math.pow(2,exp)) - 1.0)) * 8388608)
                return ((((-2147483648 if ((f < 0)) else 0)) | (((exp + 127) << 23))) | Math.floor((af + 0.5)))

    @staticmethod
    def i64ToDouble(low,high):
        sign = (1 - ((HxOverrides.rshift(high, 31) << 1)))
        e = ((high >> 20) & 2047)
        if (e == 2047):
            if ((low == 0) and ((((high & 1048575)) == 0))):
                if (sign > 0):
                    return Math.POSITIVE_INFINITY
                else:
                    return Math.NEGATIVE_INFINITY
            else:
                return Math.NaN
        else:
            m = (2.220446049250313e-16 * ((((((high & 1048575)) * 4294967296.) + (((HxOverrides.rshift(low, 31)) * 2147483648.))) + ((low & 2147483647)))))
            if (e == 0):
                m = (m * 2.0)
            else:
                m = (m + 1.0)
            return ((sign * m) * Math.pow(2,(e - 1023)))

    @staticmethod
    def doubleToI64(v):
        i64 = haxe_io_FPHelper.i64tmp
        if (v == 0):
            i64.low = 0
            i64.high = 0
        elif (not ((((v != Math.POSITIVE_INFINITY) and ((v != Math.NEGATIVE_INFINITY))) and (not python_lib_Math.isnan(v))))):
            i64.low = 0
            i64.high = (2146435072 if ((v > 0)) else -1048576)
        else:
            av = (-v if ((v < 0)) else v)
            exp = Math.floor((((Math.NEGATIVE_INFINITY if ((av == 0.0)) else (Math.NaN if ((av < 0.0)) else python_lib_Math.log(av)))) / 0.6931471805599453))
            if (exp > 1023):
                i64.low = -1
                i64.high = 2146435071
            else:
                if (exp <= -1023):
                    exp = -1023
                    av = (av / 2.2250738585072014e-308)
                else:
                    av = ((av / Math.pow(2,exp)) - 1.0)
                v1 = (av * 4503599627370496.)
                sig = (v1 if (((v1 == Math.POSITIVE_INFINITY) or ((v1 == Math.NEGATIVE_INFINITY)))) else (Math.NaN if (python_lib_Math.isnan(v1)) else Math.floor((v1 + 0.5))))
                sig_l = None
                try:
                    sig_l = int(sig)
                except BaseException as _g:
                    None
                    sig_l = None
                sig_l1 = sig_l
                sig_h = None
                try:
                    sig_h = int((sig / 4294967296.0))
                except BaseException as _g:
                    None
                    sig_h = None
                sig_h1 = sig_h
                i64.low = sig_l1
                i64.high = ((((-2147483648 if ((v < 0)) else 0)) | (((exp + 1023) << 20))) | sig_h1)
        return i64
haxe_io_FPHelper._hx_class = haxe_io_FPHelper
_hx_classes["haxe.io.FPHelper"] = haxe_io_FPHelper


class haxe_io_Input:
    _hx_class_name = "haxe.io.Input"
    __slots__ = ("bigEndian",)
    _hx_fields = ["bigEndian"]
    _hx_methods = ["readByte", "readBytes", "close", "set_bigEndian", "readAll", "readFullBytes", "read", "readUntil", "readLine", "readFloat", "readDouble", "readInt8", "readInt16", "readUInt16", "readInt24", "readUInt24", "readInt32", "readString", "getDoubleSig"]

    def readByte(self):
        raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "haxe/io/Input.hx", 'lineNumber': 53, 'className': "haxe.io.Input", 'methodName': "readByte"}))

    def readBytes(self,s,pos,_hx_len):
        k = _hx_len
        b = s.b
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > s.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        try:
            while (k > 0):
                b[pos] = self.readByte()
                pos = (pos + 1)
                k = (k - 1)
        except BaseException as _g:
            None
            if (not Std.isOfType(haxe_Exception.caught(_g).unwrap(),haxe_io_Eof)):
                raise _g
        return (_hx_len - k)

    def close(self):
        pass

    def set_bigEndian(self,b):
        self.bigEndian = b
        return b

    def readAll(self,bufsize = None):
        if (bufsize is None):
            bufsize = 16384
        buf = haxe_io_Bytes.alloc(bufsize)
        total = haxe_io_BytesBuffer()
        try:
            while True:
                _hx_len = self.readBytes(buf,0,bufsize)
                if (_hx_len == 0):
                    raise haxe_Exception.thrown(haxe_io_Error.Blocked)
                if ((_hx_len < 0) or ((_hx_len > buf.length))):
                    raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
                total.b.extend(buf.b[0:_hx_len])
        except BaseException as _g:
            None
            if (not Std.isOfType(haxe_Exception.caught(_g).unwrap(),haxe_io_Eof)):
                raise _g
        return total.getBytes()

    def readFullBytes(self,s,pos,_hx_len):
        while (_hx_len > 0):
            k = self.readBytes(s,pos,_hx_len)
            if (k == 0):
                raise haxe_Exception.thrown(haxe_io_Error.Blocked)
            pos = (pos + k)
            _hx_len = (_hx_len - k)

    def read(self,nbytes):
        s = haxe_io_Bytes.alloc(nbytes)
        p = 0
        while (nbytes > 0):
            k = self.readBytes(s,p,nbytes)
            if (k == 0):
                raise haxe_Exception.thrown(haxe_io_Error.Blocked)
            p = (p + k)
            nbytes = (nbytes - k)
        return s

    def readUntil(self,end):
        buf = haxe_io_BytesBuffer()
        last = None
        while True:
            last = self.readByte()
            if (not ((last != end))):
                break
            buf.b.append(last)
        return buf.getBytes().toString()

    def readLine(self):
        buf = haxe_io_BytesBuffer()
        last = None
        s = None
        try:
            while True:
                last = self.readByte()
                if (not ((last != 10))):
                    break
                buf.b.append(last)
            s = buf.getBytes().toString()
            if (HxString.charCodeAt(s,(len(s) - 1)) == 13):
                s = HxString.substr(s,0,-1)
        except BaseException as _g:
            None
            _g1 = haxe_Exception.caught(_g).unwrap()
            if Std.isOfType(_g1,haxe_io_Eof):
                e = _g1
                s = buf.getBytes().toString()
                if (len(s) == 0):
                    raise haxe_Exception.thrown(e)
            else:
                raise _g
        return s

    def readFloat(self):
        return haxe_io_FPHelper.i32ToFloat(self.readInt32())

    def readDouble(self):
        i1 = self.readInt32()
        i2 = self.readInt32()
        if self.bigEndian:
            return haxe_io_FPHelper.i64ToDouble(i2,i1)
        else:
            return haxe_io_FPHelper.i64ToDouble(i1,i2)

    def readInt8(self):
        n = self.readByte()
        if (n >= 128):
            return (n - 256)
        return n

    def readInt16(self):
        ch1 = self.readByte()
        ch2 = self.readByte()
        n = ((ch2 | ((ch1 << 8))) if (self.bigEndian) else (ch1 | ((ch2 << 8))))
        if (((n & 32768)) != 0):
            return (n - 65536)
        return n

    def readUInt16(self):
        ch1 = self.readByte()
        ch2 = self.readByte()
        if self.bigEndian:
            return (ch2 | ((ch1 << 8)))
        else:
            return (ch1 | ((ch2 << 8)))

    def readInt24(self):
        ch1 = self.readByte()
        ch2 = self.readByte()
        ch3 = self.readByte()
        n = (((ch3 | ((ch2 << 8))) | ((ch1 << 16))) if (self.bigEndian) else ((ch1 | ((ch2 << 8))) | ((ch3 << 16))))
        if (((n & 8388608)) != 0):
            return (n - 16777216)
        return n

    def readUInt24(self):
        ch1 = self.readByte()
        ch2 = self.readByte()
        ch3 = self.readByte()
        if self.bigEndian:
            return ((ch3 | ((ch2 << 8))) | ((ch1 << 16)))
        else:
            return ((ch1 | ((ch2 << 8))) | ((ch3 << 16)))

    def readInt32(self):
        ch1 = self.readByte()
        ch2 = self.readByte()
        ch3 = self.readByte()
        ch4 = self.readByte()
        n = ((((ch4 | ((ch3 << 8))) | ((ch2 << 16))) | ((ch1 << 24))) if (self.bigEndian) else (((ch1 | ((ch2 << 8))) | ((ch3 << 16))) | ((ch4 << 24))))
        if (((n & -2147483648)) != 0):
            return (n | -2147483648)
        else:
            return n

    def readString(self,_hx_len,encoding = None):
        b = haxe_io_Bytes.alloc(_hx_len)
        self.readFullBytes(b,0,_hx_len)
        return b.getString(0,_hx_len,encoding)

    def getDoubleSig(self,_hx_bytes):
        return ((((((((((_hx_bytes[1] if 1 < len(_hx_bytes) else None) & 15)) << 16) | (((_hx_bytes[2] if 2 < len(_hx_bytes) else None) << 8))) | (_hx_bytes[3] if 3 < len(_hx_bytes) else None))) * 4294967296.) + (((((_hx_bytes[4] if 4 < len(_hx_bytes) else None) >> 7)) * 2147483648))) + ((((((((_hx_bytes[4] if 4 < len(_hx_bytes) else None) & 127)) << 24) | (((_hx_bytes[5] if 5 < len(_hx_bytes) else None) << 16))) | (((_hx_bytes[6] if 6 < len(_hx_bytes) else None) << 8))) | (_hx_bytes[7] if 7 < len(_hx_bytes) else None))))

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.bigEndian = None
haxe_io_Input._hx_class = haxe_io_Input
_hx_classes["haxe.io.Input"] = haxe_io_Input


class haxe_io_Output:
    _hx_class_name = "haxe.io.Output"
    __slots__ = ("bigEndian",)
    _hx_fields = ["bigEndian"]
    _hx_methods = ["writeByte", "writeBytes", "flush", "close", "set_bigEndian", "write", "writeFullBytes", "writeFloat", "writeDouble", "writeInt8", "writeInt16", "writeUInt16", "writeInt24", "writeUInt24", "writeInt32", "prepare", "writeInput", "writeString"]

    def writeByte(self,c):
        raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "haxe/io/Output.hx", 'lineNumber': 47, 'className': "haxe.io.Output", 'methodName': "writeByte"}))

    def writeBytes(self,s,pos,_hx_len):
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > s.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        b = s.b
        k = _hx_len
        while (k > 0):
            self.writeByte(b[pos])
            pos = (pos + 1)
            k = (k - 1)
        return _hx_len

    def flush(self):
        pass

    def close(self):
        pass

    def set_bigEndian(self,b):
        self.bigEndian = b
        return b

    def write(self,s):
        l = s.length
        p = 0
        while (l > 0):
            k = self.writeBytes(s,p,l)
            if (k == 0):
                raise haxe_Exception.thrown(haxe_io_Error.Blocked)
            p = (p + k)
            l = (l - k)

    def writeFullBytes(self,s,pos,_hx_len):
        while (_hx_len > 0):
            k = self.writeBytes(s,pos,_hx_len)
            pos = (pos + k)
            _hx_len = (_hx_len - k)

    def writeFloat(self,x):
        self.writeInt32(haxe_io_FPHelper.floatToI32(x))

    def writeDouble(self,x):
        i64 = haxe_io_FPHelper.doubleToI64(x)
        if self.bigEndian:
            self.writeInt32(i64.high)
            self.writeInt32(i64.low)
        else:
            self.writeInt32(i64.low)
            self.writeInt32(i64.high)

    def writeInt8(self,x):
        if ((x < -128) or ((x >= 128))):
            raise haxe_Exception.thrown(haxe_io_Error.Overflow)
        self.writeByte((x & 255))

    def writeInt16(self,x):
        if ((x < -32768) or ((x >= 32768))):
            raise haxe_Exception.thrown(haxe_io_Error.Overflow)
        self.writeUInt16((x & 65535))

    def writeUInt16(self,x):
        if ((x < 0) or ((x >= 65536))):
            raise haxe_Exception.thrown(haxe_io_Error.Overflow)
        if self.bigEndian:
            self.writeByte((x >> 8))
            self.writeByte((x & 255))
        else:
            self.writeByte((x & 255))
            self.writeByte((x >> 8))

    def writeInt24(self,x):
        if ((x < -8388608) or ((x >= 8388608))):
            raise haxe_Exception.thrown(haxe_io_Error.Overflow)
        self.writeUInt24((x & 16777215))

    def writeUInt24(self,x):
        if ((x < 0) or ((x >= 16777216))):
            raise haxe_Exception.thrown(haxe_io_Error.Overflow)
        if self.bigEndian:
            self.writeByte((x >> 16))
            self.writeByte(((x >> 8) & 255))
            self.writeByte((x & 255))
        else:
            self.writeByte((x & 255))
            self.writeByte(((x >> 8) & 255))
            self.writeByte((x >> 16))

    def writeInt32(self,x):
        if self.bigEndian:
            self.writeByte(HxOverrides.rshift(x, 24))
            self.writeByte(((x >> 16) & 255))
            self.writeByte(((x >> 8) & 255))
            self.writeByte((x & 255))
        else:
            self.writeByte((x & 255))
            self.writeByte(((x >> 8) & 255))
            self.writeByte(((x >> 16) & 255))
            self.writeByte(HxOverrides.rshift(x, 24))

    def prepare(self,nbytes):
        pass

    def writeInput(self,i,bufsize = None):
        if (bufsize is None):
            bufsize = 4096
        buf = haxe_io_Bytes.alloc(bufsize)
        try:
            while True:
                _hx_len = i.readBytes(buf,0,bufsize)
                if (_hx_len == 0):
                    raise haxe_Exception.thrown(haxe_io_Error.Blocked)
                p = 0
                while (_hx_len > 0):
                    k = self.writeBytes(buf,p,_hx_len)
                    if (k == 0):
                        raise haxe_Exception.thrown(haxe_io_Error.Blocked)
                    p = (p + k)
                    _hx_len = (_hx_len - k)
        except BaseException as _g:
            None
            if (not Std.isOfType(haxe_Exception.caught(_g).unwrap(),haxe_io_Eof)):
                raise _g

    def writeString(self,s,encoding = None):
        b = haxe_io_Bytes.ofString(s,encoding)
        self.writeFullBytes(b,0,b.length)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.bigEndian = None
haxe_io_Output._hx_class = haxe_io_Output
_hx_classes["haxe.io.Output"] = haxe_io_Output


class haxe_io_Path:
    _hx_class_name = "haxe.io.Path"
    __slots__ = ("dir", "file", "ext", "backslash")
    _hx_fields = ["dir", "file", "ext", "backslash"]
    _hx_methods = ["toString"]
    _hx_statics = ["withoutExtension", "withoutDirectory", "directory", "extension", "withExtension", "join", "normalize", "addTrailingSlash", "removeTrailingSlashes", "isAbsolute", "unescape", "escape"]

    def __init__(self,path):
        self.backslash = None
        self.ext = None
        self.file = None
        self.dir = None
        path1 = path
        _hx_local_0 = len(path1)
        if (_hx_local_0 == 1):
            if (path1 == "."):
                self.dir = path
                self.file = ""
                return
        elif (_hx_local_0 == 2):
            if (path1 == ".."):
                self.dir = path
                self.file = ""
                return
        else:
            pass
        startIndex = None
        c1 = None
        if (startIndex is None):
            c1 = path.rfind("/", 0, len(path))
        else:
            i = path.rfind("/", 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len("/"))) if ((i == -1)) else (i + 1))
            check = path.find("/", startLeft, len(path))
            c1 = (check if (((check > i) and ((check <= startIndex)))) else i)
        startIndex = None
        c2 = None
        if (startIndex is None):
            c2 = path.rfind("\\", 0, len(path))
        else:
            i = path.rfind("\\", 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len("\\"))) if ((i == -1)) else (i + 1))
            check = path.find("\\", startLeft, len(path))
            c2 = (check if (((check > i) and ((check <= startIndex)))) else i)
        if (c1 < c2):
            self.dir = HxString.substr(path,0,c2)
            path = HxString.substr(path,(c2 + 1),None)
            self.backslash = True
        elif (c2 < c1):
            self.dir = HxString.substr(path,0,c1)
            path = HxString.substr(path,(c1 + 1),None)
        else:
            self.dir = None
        startIndex = None
        cp = None
        if (startIndex is None):
            cp = path.rfind(".", 0, len(path))
        else:
            i = path.rfind(".", 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len("."))) if ((i == -1)) else (i + 1))
            check = path.find(".", startLeft, len(path))
            cp = (check if (((check > i) and ((check <= startIndex)))) else i)
        if (cp != -1):
            self.ext = HxString.substr(path,(cp + 1),None)
            self.file = HxString.substr(path,0,cp)
        else:
            self.ext = None
            self.file = path

    def toString(self):
        return ((HxOverrides.stringOrNull((("" if ((self.dir is None)) else (HxOverrides.stringOrNull(self.dir) + HxOverrides.stringOrNull((("\\" if (self.backslash) else "/"))))))) + HxOverrides.stringOrNull(self.file)) + HxOverrides.stringOrNull((("" if ((self.ext is None)) else ("." + HxOverrides.stringOrNull(self.ext))))))

    @staticmethod
    def withoutExtension(path):
        s = haxe_io_Path(path)
        s.ext = None
        return s.toString()

    @staticmethod
    def withoutDirectory(path):
        s = haxe_io_Path(path)
        s.dir = None
        return s.toString()

    @staticmethod
    def directory(path):
        s = haxe_io_Path(path)
        if (s.dir is None):
            return ""
        return s.dir

    @staticmethod
    def extension(path):
        s = haxe_io_Path(path)
        if (s.ext is None):
            return ""
        return s.ext

    @staticmethod
    def withExtension(path,ext):
        s = haxe_io_Path(path)
        s.ext = ext
        return s.toString()

    @staticmethod
    def join(paths):
        def _hx_local_0(s):
            if (s is not None):
                return (s != "")
            else:
                return False
        paths1 = list(filter(_hx_local_0,paths))
        if (len(paths1) == 0):
            return ""
        path = (paths1[0] if 0 < len(paths1) else None)
        _g = 1
        _g1 = len(paths1)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            path = haxe_io_Path.addTrailingSlash(path)
            path = (("null" if path is None else path) + HxOverrides.stringOrNull((paths1[i] if i >= 0 and i < len(paths1) else None)))
        return haxe_io_Path.normalize(path)

    @staticmethod
    def normalize(path):
        slash = "/"
        _this = path.split("\\")
        path = slash.join([python_Boot.toString1(x1,'') for x1 in _this])
        if (path == slash):
            return slash
        target = []
        _g = 0
        _g1 = (list(path) if ((slash == "")) else path.split(slash))
        while (_g < len(_g1)):
            token = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            if (((token == "..") and ((len(target) > 0))) and ((python_internal_ArrayImpl._get(target, (len(target) - 1)) != ".."))):
                if (len(target) != 0):
                    target.pop()
            elif (token == ""):
                if ((len(target) > 0) or ((HxString.charCodeAt(path,0) == 47))):
                    target.append(token)
            elif (token != "."):
                target.append(token)
        tmp = slash.join([python_Boot.toString1(x1,'') for x1 in target])
        acc_b = python_lib_io_StringIO()
        colon = False
        slashes = False
        _g = 0
        _g1 = len(tmp)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            _g2 = (-1 if ((i >= len(tmp))) else ord(tmp[i]))
            _g3 = _g2
            if (_g3 == 47):
                if (not colon):
                    slashes = True
                else:
                    i1 = _g2
                    colon = False
                    if slashes:
                        acc_b.write("/")
                        slashes = False
                    acc_b.write("".join(map(chr,[i1])))
            elif (_g3 == 58):
                acc_b.write(":")
                colon = True
            else:
                i2 = _g2
                colon = False
                if slashes:
                    acc_b.write("/")
                    slashes = False
                acc_b.write("".join(map(chr,[i2])))
        return acc_b.getvalue()

    @staticmethod
    def addTrailingSlash(path):
        if (len(path) == 0):
            return "/"
        startIndex = None
        c1 = None
        if (startIndex is None):
            c1 = path.rfind("/", 0, len(path))
        else:
            i = path.rfind("/", 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len("/"))) if ((i == -1)) else (i + 1))
            check = path.find("/", startLeft, len(path))
            c1 = (check if (((check > i) and ((check <= startIndex)))) else i)
        startIndex = None
        c2 = None
        if (startIndex is None):
            c2 = path.rfind("\\", 0, len(path))
        else:
            i = path.rfind("\\", 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len("\\"))) if ((i == -1)) else (i + 1))
            check = path.find("\\", startLeft, len(path))
            c2 = (check if (((check > i) and ((check <= startIndex)))) else i)
        if (c1 < c2):
            if (c2 != ((len(path) - 1))):
                return (("null" if path is None else path) + "\\")
            else:
                return path
        elif (c1 != ((len(path) - 1))):
            return (("null" if path is None else path) + "/")
        else:
            return path

    @staticmethod
    def removeTrailingSlashes(path):
        while True:
            _g = HxString.charCodeAt(path,(len(path) - 1))
            if (_g is None):
                break
            else:
                _g1 = _g
                if ((_g1 == 92) or ((_g1 == 47))):
                    path = HxString.substr(path,0,-1)
                else:
                    break
        return path

    @staticmethod
    def isAbsolute(path):
        if path.startswith("/"):
            return True
        if ((("" if ((1 >= len(path))) else path[1])) == ":"):
            return True
        if path.startswith("\\\\"):
            return True
        return False

    @staticmethod
    def unescape(path):
        regex = EReg("-x([0-9][0-9])","g")
        def _hx_local_1():
            def _hx_local_0(regex):
                code = Std.parseInt(regex.matchObj.group(1))
                return "".join(map(chr,[code]))
            return regex.map(path,_hx_local_0)
        return _hx_local_1()

    @staticmethod
    def escape(path,allowSlashes = None):
        if (allowSlashes is None):
            allowSlashes = False
        regex = (EReg("[^A-Za-z0-9_/\\\\\\.]","g") if allowSlashes else EReg("[^A-Za-z0-9_\\.]","g"))
        def _hx_local_1():
            def _hx_local_0(v):
                return ("-x" + Std.string(HxString.charCodeAt(v.matchObj.group(0),0)))
            return regex.map(path,_hx_local_0)
        return _hx_local_1()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.dir = None
        _hx_o.file = None
        _hx_o.ext = None
        _hx_o.backslash = None
haxe_io_Path._hx_class = haxe_io_Path
_hx_classes["haxe.io.Path"] = haxe_io_Path


class haxe_iterators_ArrayIterator:
    _hx_class_name = "haxe.iterators.ArrayIterator"
    __slots__ = ("array", "current")
    _hx_fields = ["array", "current"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,array):
        self.current = 0
        self.array = array

    def hasNext(self):
        return (self.current < len(self.array))

    def next(self):
        def _hx_local_3():
            def _hx_local_2():
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.current
                _hx_local_0.current = (_hx_local_1 + 1)
                return _hx_local_1
            return python_internal_ArrayImpl._get(self.array, _hx_local_2())
        return _hx_local_3()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.array = None
        _hx_o.current = None
haxe_iterators_ArrayIterator._hx_class = haxe_iterators_ArrayIterator
_hx_classes["haxe.iterators.ArrayIterator"] = haxe_iterators_ArrayIterator


class haxe_iterators_ArrayKeyValueIterator:
    _hx_class_name = "haxe.iterators.ArrayKeyValueIterator"
    __slots__ = ("current", "array")
    _hx_fields = ["current", "array"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,array):
        self.current = 0
        self.array = array

    def hasNext(self):
        return (self.current < len(self.array))

    def next(self):
        def _hx_local_3():
            def _hx_local_2():
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.current
                _hx_local_0.current = (_hx_local_1 + 1)
                return _hx_local_1
            return _hx_AnonObject({'value': python_internal_ArrayImpl._get(self.array, self.current), 'key': _hx_local_2()})
        return _hx_local_3()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.current = None
        _hx_o.array = None
haxe_iterators_ArrayKeyValueIterator._hx_class = haxe_iterators_ArrayKeyValueIterator
_hx_classes["haxe.iterators.ArrayKeyValueIterator"] = haxe_iterators_ArrayKeyValueIterator


class haxe_iterators_HashMapKeyValueIterator:
    _hx_class_name = "haxe.iterators.HashMapKeyValueIterator"
    __slots__ = ("map", "keys")
    _hx_fields = ["map", "keys"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,_hx_map):
        self.map = _hx_map
        self.keys = _hx_map.keys.iterator()

    def hasNext(self):
        return self.keys.hasNext()

    def next(self):
        key = self.keys.next()
        _this = self.map.values
        key1 = key.hashCode()
        return _hx_AnonObject({'value': _this.h.get(key1,None), 'key': key})

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.map = None
        _hx_o.keys = None
haxe_iterators_HashMapKeyValueIterator._hx_class = haxe_iterators_HashMapKeyValueIterator
_hx_classes["haxe.iterators.HashMapKeyValueIterator"] = haxe_iterators_HashMapKeyValueIterator


class haxe_iterators_MapKeyValueIterator:
    _hx_class_name = "haxe.iterators.MapKeyValueIterator"
    __slots__ = ("map", "keys")
    _hx_fields = ["map", "keys"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,_hx_map):
        self.map = _hx_map
        self.keys = _hx_map.keys()

    def hasNext(self):
        return self.keys.hasNext()

    def next(self):
        key = self.keys.next()
        return _hx_AnonObject({'value': self.map.get(key), 'key': key})

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.map = None
        _hx_o.keys = None
haxe_iterators_MapKeyValueIterator._hx_class = haxe_iterators_MapKeyValueIterator
_hx_classes["haxe.iterators.MapKeyValueIterator"] = haxe_iterators_MapKeyValueIterator


class haxe_iterators_RestIterator:
    _hx_class_name = "haxe.iterators.RestIterator"
    __slots__ = ("args", "current")
    _hx_fields = ["args", "current"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,args):
        self.current = 0
        self.args = args

    def hasNext(self):
        return (self.current < len(self.args))

    def next(self):
        index = self.current
        self.current = (self.current + 1)
        return python_internal_ArrayImpl._get(self.args, index)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.args = None
        _hx_o.current = None
haxe_iterators_RestIterator._hx_class = haxe_iterators_RestIterator
_hx_classes["haxe.iterators.RestIterator"] = haxe_iterators_RestIterator


class haxe_iterators_RestKeyValueIterator:
    _hx_class_name = "haxe.iterators.RestKeyValueIterator"
    __slots__ = ("args", "current")
    _hx_fields = ["args", "current"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,args):
        self.current = 0
        self.args = args

    def hasNext(self):
        return (self.current < len(self.args))

    def next(self):
        tmp = self.current
        index = self.current
        self.current = (self.current + 1)
        return _hx_AnonObject({'key': tmp, 'value': python_internal_ArrayImpl._get(self.args, index)})

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.args = None
        _hx_o.current = None
haxe_iterators_RestKeyValueIterator._hx_class = haxe_iterators_RestKeyValueIterator
_hx_classes["haxe.iterators.RestKeyValueIterator"] = haxe_iterators_RestKeyValueIterator


class haxe_iterators_StringIterator:
    _hx_class_name = "haxe.iterators.StringIterator"
    __slots__ = ("offset", "s")
    _hx_fields = ["offset", "s"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,s):
        self.offset = 0
        self.s = s

    def hasNext(self):
        return (self.offset < len(self.s))

    def next(self):
        index = self.offset
        self.offset = (self.offset + 1)
        return ord(self.s[index])

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.offset = None
        _hx_o.s = None
haxe_iterators_StringIterator._hx_class = haxe_iterators_StringIterator
_hx_classes["haxe.iterators.StringIterator"] = haxe_iterators_StringIterator


class haxe_iterators_StringIteratorUnicode:
    _hx_class_name = "haxe.iterators.StringIteratorUnicode"
    __slots__ = ("offset", "s")
    _hx_fields = ["offset", "s"]
    _hx_methods = ["hasNext", "next"]
    _hx_statics = ["unicodeIterator"]

    def __init__(self,s):
        self.offset = 0
        self.s = s

    def hasNext(self):
        return (self.offset < len(self.s))

    def next(self):
        index = self.offset
        self.offset = (self.offset + 1)
        return ord(self.s[index])

    @staticmethod
    def unicodeIterator(s):
        return haxe_iterators_StringIteratorUnicode(s)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.offset = None
        _hx_o.s = None
haxe_iterators_StringIteratorUnicode._hx_class = haxe_iterators_StringIteratorUnicode
_hx_classes["haxe.iterators.StringIteratorUnicode"] = haxe_iterators_StringIteratorUnicode


class haxe_iterators_StringKeyValueIterator:
    _hx_class_name = "haxe.iterators.StringKeyValueIterator"
    __slots__ = ("offset", "s")
    _hx_fields = ["offset", "s"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,s):
        self.offset = 0
        self.s = s

    def hasNext(self):
        return (self.offset < len(self.s))

    def next(self):
        tmp = self.offset
        s = self.s
        index = self.offset
        self.offset = (self.offset + 1)
        return _hx_AnonObject({'key': tmp, 'value': (-1 if ((index >= len(s))) else ord(s[index]))})

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.offset = None
        _hx_o.s = None
haxe_iterators_StringKeyValueIterator._hx_class = haxe_iterators_StringKeyValueIterator
_hx_classes["haxe.iterators.StringKeyValueIterator"] = haxe_iterators_StringKeyValueIterator


class haxe_macro_ComplexTypeTools:
    _hx_class_name = "haxe.macro.ComplexTypeTools"
    __slots__ = ()
    _hx_statics = ["toString"]

    @staticmethod
    def toString(c):
        return haxe_macro_Printer().printComplexType(c)
haxe_macro_ComplexTypeTools._hx_class = haxe_macro_ComplexTypeTools
_hx_classes["haxe.macro.ComplexTypeTools"] = haxe_macro_ComplexTypeTools

class haxe_macro_Message(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.Message"
    _hx_constructs = ["Info", "Warning"]

    @staticmethod
    def Info(msg,pos):
        return haxe_macro_Message("Info", 0, (msg,pos))

    @staticmethod
    def Warning(msg,pos):
        return haxe_macro_Message("Warning", 1, (msg,pos))
haxe_macro_Message._hx_class = haxe_macro_Message
_hx_classes["haxe.macro.Message"] = haxe_macro_Message


class haxe_macro_Context:
    _hx_class_name = "haxe.macro.Context"
    __slots__ = ()
haxe_macro_Context._hx_class = haxe_macro_Context
_hx_classes["haxe.macro.Context"] = haxe_macro_Context

class haxe_macro_StringLiteralKind(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.StringLiteralKind"
    _hx_constructs = ["DoubleQuotes", "SingleQuotes"]
haxe_macro_StringLiteralKind.DoubleQuotes = haxe_macro_StringLiteralKind("DoubleQuotes", 0, ())
haxe_macro_StringLiteralKind.SingleQuotes = haxe_macro_StringLiteralKind("SingleQuotes", 1, ())
haxe_macro_StringLiteralKind._hx_class = haxe_macro_StringLiteralKind
_hx_classes["haxe.macro.StringLiteralKind"] = haxe_macro_StringLiteralKind

class haxe_macro_Constant(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.Constant"
    _hx_constructs = ["CInt", "CFloat", "CString", "CIdent", "CRegexp"]

    @staticmethod
    def CInt(v):
        return haxe_macro_Constant("CInt", 0, (v,))

    @staticmethod
    def CFloat(f):
        return haxe_macro_Constant("CFloat", 1, (f,))

    @staticmethod
    def CString(s,kind = None):
        return haxe_macro_Constant("CString", 2, (s,kind))

    @staticmethod
    def CIdent(s):
        return haxe_macro_Constant("CIdent", 3, (s,))

    @staticmethod
    def CRegexp(r,opt):
        return haxe_macro_Constant("CRegexp", 4, (r,opt))
haxe_macro_Constant._hx_class = haxe_macro_Constant
_hx_classes["haxe.macro.Constant"] = haxe_macro_Constant

class haxe_macro_Binop(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.Binop"
    _hx_constructs = ["OpAdd", "OpMult", "OpDiv", "OpSub", "OpAssign", "OpEq", "OpNotEq", "OpGt", "OpGte", "OpLt", "OpLte", "OpAnd", "OpOr", "OpXor", "OpBoolAnd", "OpBoolOr", "OpShl", "OpShr", "OpUShr", "OpMod", "OpAssignOp", "OpInterval", "OpArrow", "OpIn"]

    @staticmethod
    def OpAssignOp(op):
        return haxe_macro_Binop("OpAssignOp", 20, (op,))
haxe_macro_Binop.OpAdd = haxe_macro_Binop("OpAdd", 0, ())
haxe_macro_Binop.OpMult = haxe_macro_Binop("OpMult", 1, ())
haxe_macro_Binop.OpDiv = haxe_macro_Binop("OpDiv", 2, ())
haxe_macro_Binop.OpSub = haxe_macro_Binop("OpSub", 3, ())
haxe_macro_Binop.OpAssign = haxe_macro_Binop("OpAssign", 4, ())
haxe_macro_Binop.OpEq = haxe_macro_Binop("OpEq", 5, ())
haxe_macro_Binop.OpNotEq = haxe_macro_Binop("OpNotEq", 6, ())
haxe_macro_Binop.OpGt = haxe_macro_Binop("OpGt", 7, ())
haxe_macro_Binop.OpGte = haxe_macro_Binop("OpGte", 8, ())
haxe_macro_Binop.OpLt = haxe_macro_Binop("OpLt", 9, ())
haxe_macro_Binop.OpLte = haxe_macro_Binop("OpLte", 10, ())
haxe_macro_Binop.OpAnd = haxe_macro_Binop("OpAnd", 11, ())
haxe_macro_Binop.OpOr = haxe_macro_Binop("OpOr", 12, ())
haxe_macro_Binop.OpXor = haxe_macro_Binop("OpXor", 13, ())
haxe_macro_Binop.OpBoolAnd = haxe_macro_Binop("OpBoolAnd", 14, ())
haxe_macro_Binop.OpBoolOr = haxe_macro_Binop("OpBoolOr", 15, ())
haxe_macro_Binop.OpShl = haxe_macro_Binop("OpShl", 16, ())
haxe_macro_Binop.OpShr = haxe_macro_Binop("OpShr", 17, ())
haxe_macro_Binop.OpUShr = haxe_macro_Binop("OpUShr", 18, ())
haxe_macro_Binop.OpMod = haxe_macro_Binop("OpMod", 19, ())
haxe_macro_Binop.OpInterval = haxe_macro_Binop("OpInterval", 21, ())
haxe_macro_Binop.OpArrow = haxe_macro_Binop("OpArrow", 22, ())
haxe_macro_Binop.OpIn = haxe_macro_Binop("OpIn", 23, ())
haxe_macro_Binop._hx_class = haxe_macro_Binop
_hx_classes["haxe.macro.Binop"] = haxe_macro_Binop

class haxe_macro_Unop(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.Unop"
    _hx_constructs = ["OpIncrement", "OpDecrement", "OpNot", "OpNeg", "OpNegBits", "OpSpread"]
haxe_macro_Unop.OpIncrement = haxe_macro_Unop("OpIncrement", 0, ())
haxe_macro_Unop.OpDecrement = haxe_macro_Unop("OpDecrement", 1, ())
haxe_macro_Unop.OpNot = haxe_macro_Unop("OpNot", 2, ())
haxe_macro_Unop.OpNeg = haxe_macro_Unop("OpNeg", 3, ())
haxe_macro_Unop.OpNegBits = haxe_macro_Unop("OpNegBits", 4, ())
haxe_macro_Unop.OpSpread = haxe_macro_Unop("OpSpread", 5, ())
haxe_macro_Unop._hx_class = haxe_macro_Unop
_hx_classes["haxe.macro.Unop"] = haxe_macro_Unop

class haxe_macro_QuoteStatus(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.QuoteStatus"
    _hx_constructs = ["Unquoted", "Quoted"]
haxe_macro_QuoteStatus.Unquoted = haxe_macro_QuoteStatus("Unquoted", 0, ())
haxe_macro_QuoteStatus.Quoted = haxe_macro_QuoteStatus("Quoted", 1, ())
haxe_macro_QuoteStatus._hx_class = haxe_macro_QuoteStatus
_hx_classes["haxe.macro.QuoteStatus"] = haxe_macro_QuoteStatus

class haxe_macro_FunctionKind(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.FunctionKind"
    _hx_constructs = ["FAnonymous", "FNamed", "FArrow"]

    @staticmethod
    def FNamed(name,inlined = None):
        return haxe_macro_FunctionKind("FNamed", 1, (name,inlined))
haxe_macro_FunctionKind.FAnonymous = haxe_macro_FunctionKind("FAnonymous", 0, ())
haxe_macro_FunctionKind.FArrow = haxe_macro_FunctionKind("FArrow", 2, ())
haxe_macro_FunctionKind._hx_class = haxe_macro_FunctionKind
_hx_classes["haxe.macro.FunctionKind"] = haxe_macro_FunctionKind

class haxe_macro_ExprDef(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.ExprDef"
    _hx_constructs = ["EConst", "EArray", "EBinop", "EField", "EParenthesis", "EObjectDecl", "EArrayDecl", "ECall", "ENew", "EUnop", "EVars", "EFunction", "EBlock", "EFor", "EIf", "EWhile", "ESwitch", "ETry", "EReturn", "EBreak", "EContinue", "EUntyped", "EThrow", "ECast", "EDisplay", "EDisplayNew", "ETernary", "ECheckType", "EMeta", "EIs"]

    @staticmethod
    def EConst(c):
        return haxe_macro_ExprDef("EConst", 0, (c,))

    @staticmethod
    def EArray(e1,e2):
        return haxe_macro_ExprDef("EArray", 1, (e1,e2))

    @staticmethod
    def EBinop(op,e1,e2):
        return haxe_macro_ExprDef("EBinop", 2, (op,e1,e2))

    @staticmethod
    def EField(e,field):
        return haxe_macro_ExprDef("EField", 3, (e,field))

    @staticmethod
    def EParenthesis(e):
        return haxe_macro_ExprDef("EParenthesis", 4, (e,))

    @staticmethod
    def EObjectDecl(fields):
        return haxe_macro_ExprDef("EObjectDecl", 5, (fields,))

    @staticmethod
    def EArrayDecl(values):
        return haxe_macro_ExprDef("EArrayDecl", 6, (values,))

    @staticmethod
    def ECall(e,params):
        return haxe_macro_ExprDef("ECall", 7, (e,params))

    @staticmethod
    def ENew(t,params):
        return haxe_macro_ExprDef("ENew", 8, (t,params))

    @staticmethod
    def EUnop(op,postFix,e):
        return haxe_macro_ExprDef("EUnop", 9, (op,postFix,e))

    @staticmethod
    def EVars(vars):
        return haxe_macro_ExprDef("EVars", 10, (vars,))

    @staticmethod
    def EFunction(kind,f):
        return haxe_macro_ExprDef("EFunction", 11, (kind,f))

    @staticmethod
    def EBlock(exprs):
        return haxe_macro_ExprDef("EBlock", 12, (exprs,))

    @staticmethod
    def EFor(it,expr):
        return haxe_macro_ExprDef("EFor", 13, (it,expr))

    @staticmethod
    def EIf(econd,eif,eelse):
        return haxe_macro_ExprDef("EIf", 14, (econd,eif,eelse))

    @staticmethod
    def EWhile(econd,e,normalWhile):
        return haxe_macro_ExprDef("EWhile", 15, (econd,e,normalWhile))

    @staticmethod
    def ESwitch(e,cases,edef):
        return haxe_macro_ExprDef("ESwitch", 16, (e,cases,edef))

    @staticmethod
    def ETry(e,catches):
        return haxe_macro_ExprDef("ETry", 17, (e,catches))

    @staticmethod
    def EReturn(e = None):
        return haxe_macro_ExprDef("EReturn", 18, (e,))

    @staticmethod
    def EUntyped(e):
        return haxe_macro_ExprDef("EUntyped", 21, (e,))

    @staticmethod
    def EThrow(e):
        return haxe_macro_ExprDef("EThrow", 22, (e,))

    @staticmethod
    def ECast(e,t):
        return haxe_macro_ExprDef("ECast", 23, (e,t))

    @staticmethod
    def EDisplay(e,displayKind):
        return haxe_macro_ExprDef("EDisplay", 24, (e,displayKind))

    @staticmethod
    def EDisplayNew(t):
        return haxe_macro_ExprDef("EDisplayNew", 25, (t,))

    @staticmethod
    def ETernary(econd,eif,eelse):
        return haxe_macro_ExprDef("ETernary", 26, (econd,eif,eelse))

    @staticmethod
    def ECheckType(e,t):
        return haxe_macro_ExprDef("ECheckType", 27, (e,t))

    @staticmethod
    def EMeta(s,e):
        return haxe_macro_ExprDef("EMeta", 28, (s,e))

    @staticmethod
    def EIs(e,t):
        return haxe_macro_ExprDef("EIs", 29, (e,t))
haxe_macro_ExprDef.EBreak = haxe_macro_ExprDef("EBreak", 19, ())
haxe_macro_ExprDef.EContinue = haxe_macro_ExprDef("EContinue", 20, ())
haxe_macro_ExprDef._hx_class = haxe_macro_ExprDef
_hx_classes["haxe.macro.ExprDef"] = haxe_macro_ExprDef

class haxe_macro_DisplayKind(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.DisplayKind"
    _hx_constructs = ["DKCall", "DKDot", "DKStructure", "DKMarked", "DKPattern"]

    @staticmethod
    def DKPattern(outermost):
        return haxe_macro_DisplayKind("DKPattern", 4, (outermost,))
haxe_macro_DisplayKind.DKCall = haxe_macro_DisplayKind("DKCall", 0, ())
haxe_macro_DisplayKind.DKDot = haxe_macro_DisplayKind("DKDot", 1, ())
haxe_macro_DisplayKind.DKStructure = haxe_macro_DisplayKind("DKStructure", 2, ())
haxe_macro_DisplayKind.DKMarked = haxe_macro_DisplayKind("DKMarked", 3, ())
haxe_macro_DisplayKind._hx_class = haxe_macro_DisplayKind
_hx_classes["haxe.macro.DisplayKind"] = haxe_macro_DisplayKind

class haxe_macro_ComplexType(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.ComplexType"
    _hx_constructs = ["TPath", "TFunction", "TAnonymous", "TParent", "TExtend", "TOptional", "TNamed", "TIntersection"]

    @staticmethod
    def TPath(p):
        return haxe_macro_ComplexType("TPath", 0, (p,))

    @staticmethod
    def TFunction(args,ret):
        return haxe_macro_ComplexType("TFunction", 1, (args,ret))

    @staticmethod
    def TAnonymous(fields):
        return haxe_macro_ComplexType("TAnonymous", 2, (fields,))

    @staticmethod
    def TParent(t):
        return haxe_macro_ComplexType("TParent", 3, (t,))

    @staticmethod
    def TExtend(p,fields):
        return haxe_macro_ComplexType("TExtend", 4, (p,fields))

    @staticmethod
    def TOptional(t):
        return haxe_macro_ComplexType("TOptional", 5, (t,))

    @staticmethod
    def TNamed(n,t):
        return haxe_macro_ComplexType("TNamed", 6, (n,t))

    @staticmethod
    def TIntersection(tl):
        return haxe_macro_ComplexType("TIntersection", 7, (tl,))
haxe_macro_ComplexType._hx_class = haxe_macro_ComplexType
_hx_classes["haxe.macro.ComplexType"] = haxe_macro_ComplexType

class haxe_macro_TypeParam(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.TypeParam"
    _hx_constructs = ["TPType", "TPExpr"]

    @staticmethod
    def TPType(t):
        return haxe_macro_TypeParam("TPType", 0, (t,))

    @staticmethod
    def TPExpr(e):
        return haxe_macro_TypeParam("TPExpr", 1, (e,))
haxe_macro_TypeParam._hx_class = haxe_macro_TypeParam
_hx_classes["haxe.macro.TypeParam"] = haxe_macro_TypeParam

class haxe_macro_Access(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.Access"
    _hx_constructs = ["APublic", "APrivate", "AStatic", "AOverride", "ADynamic", "AInline", "AMacro", "AFinal", "AExtern", "AAbstract", "AOverload"]
haxe_macro_Access.APublic = haxe_macro_Access("APublic", 0, ())
haxe_macro_Access.APrivate = haxe_macro_Access("APrivate", 1, ())
haxe_macro_Access.AStatic = haxe_macro_Access("AStatic", 2, ())
haxe_macro_Access.AOverride = haxe_macro_Access("AOverride", 3, ())
haxe_macro_Access.ADynamic = haxe_macro_Access("ADynamic", 4, ())
haxe_macro_Access.AInline = haxe_macro_Access("AInline", 5, ())
haxe_macro_Access.AMacro = haxe_macro_Access("AMacro", 6, ())
haxe_macro_Access.AFinal = haxe_macro_Access("AFinal", 7, ())
haxe_macro_Access.AExtern = haxe_macro_Access("AExtern", 8, ())
haxe_macro_Access.AAbstract = haxe_macro_Access("AAbstract", 9, ())
haxe_macro_Access.AOverload = haxe_macro_Access("AOverload", 10, ())
haxe_macro_Access._hx_class = haxe_macro_Access
_hx_classes["haxe.macro.Access"] = haxe_macro_Access

class haxe_macro_FieldType(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.FieldType"
    _hx_constructs = ["FVar", "FFun", "FProp"]

    @staticmethod
    def FVar(t,e = None):
        return haxe_macro_FieldType("FVar", 0, (t,e))

    @staticmethod
    def FFun(f):
        return haxe_macro_FieldType("FFun", 1, (f,))

    @staticmethod
    def FProp(get,set,t = None,e= None):
        return haxe_macro_FieldType("FProp", 2, (get,set,t,e))
haxe_macro_FieldType._hx_class = haxe_macro_FieldType
_hx_classes["haxe.macro.FieldType"] = haxe_macro_FieldType

class haxe_macro_TypeDefKind(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.TypeDefKind"
    _hx_constructs = ["TDEnum", "TDStructure", "TDClass", "TDAlias", "TDAbstract", "TDField"]

    @staticmethod
    def TDClass(superClass = None,interfaces= None,isInterface= None,isFinal= None,isAbstract= None):
        return haxe_macro_TypeDefKind("TDClass", 2, (superClass,interfaces,isInterface,isFinal,isAbstract))

    @staticmethod
    def TDAlias(t):
        return haxe_macro_TypeDefKind("TDAlias", 3, (t,))

    @staticmethod
    def TDAbstract(tthis,_hx_from = None,to= None):
        return haxe_macro_TypeDefKind("TDAbstract", 4, (tthis,_hx_from,to))

    @staticmethod
    def TDField(kind,access = None):
        return haxe_macro_TypeDefKind("TDField", 5, (kind,access))
haxe_macro_TypeDefKind.TDEnum = haxe_macro_TypeDefKind("TDEnum", 0, ())
haxe_macro_TypeDefKind.TDStructure = haxe_macro_TypeDefKind("TDStructure", 1, ())
haxe_macro_TypeDefKind._hx_class = haxe_macro_TypeDefKind
_hx_classes["haxe.macro.TypeDefKind"] = haxe_macro_TypeDefKind


class haxe_macro_Error(haxe_Exception):
    _hx_class_name = "haxe.macro.Error"
    __slots__ = ("pos",)
    _hx_fields = ["pos"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_Exception


    def __init__(self,message,pos,previous = None):
        self.pos = None
        super().__init__(message,previous)
        self.pos = pos
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0._hx___skipStack
        _hx_local_0._hx___skipStack = (_hx_local_1 + 1)
        _hx_local_1

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.pos = None
haxe_macro_Error._hx_class = haxe_macro_Error
_hx_classes["haxe.macro.Error"] = haxe_macro_Error

class haxe_macro_ImportMode(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.ImportMode"
    _hx_constructs = ["INormal", "IAsName", "IAll"]

    @staticmethod
    def IAsName(alias):
        return haxe_macro_ImportMode("IAsName", 1, (alias,))
haxe_macro_ImportMode.INormal = haxe_macro_ImportMode("INormal", 0, ())
haxe_macro_ImportMode.IAll = haxe_macro_ImportMode("IAll", 2, ())
haxe_macro_ImportMode._hx_class = haxe_macro_ImportMode
_hx_classes["haxe.macro.ImportMode"] = haxe_macro_ImportMode


class haxe_macro_Format:
    _hx_class_name = "haxe.macro.Format"
    __slots__ = ()
haxe_macro_Format._hx_class = haxe_macro_Format
_hx_classes["haxe.macro.Format"] = haxe_macro_Format


class haxe_macro_Printer:
    _hx_class_name = "haxe.macro.Printer"
    __slots__ = ("tabs", "tabString")
    _hx_fields = ["tabs", "tabString"]
    _hx_methods = ["printUnop", "printBinop", "escapeString", "printFormatString", "printString", "printConstant", "printTypeParam", "printTypePath", "printComplexType", "printMetadata", "printAccess", "printField", "printTypeParamDecl", "printFunctionArg", "printFunction", "printVar", "printObjectFieldKey", "printObjectField", "printExpr", "printExprs", "printExtension", "printStructure", "printTypeDefinition", "printFieldWithDelimiter", "opt", "printExprWithPositions"]

    def __init__(self,tabString = None):
        if (tabString is None):
            tabString = "\t"
        self.tabs = ""
        self.tabString = tabString

    def printUnop(self,op):
        tmp = op.index
        if (tmp == 0):
            return "++"
        elif (tmp == 1):
            return "--"
        elif (tmp == 2):
            return "!"
        elif (tmp == 3):
            return "-"
        elif (tmp == 4):
            return "~"
        elif (tmp == 5):
            return "..."
        else:
            pass

    def printBinop(self,op):
        tmp = op.index
        if (tmp == 0):
            return "+"
        elif (tmp == 1):
            return "*"
        elif (tmp == 2):
            return "/"
        elif (tmp == 3):
            return "-"
        elif (tmp == 4):
            return "="
        elif (tmp == 5):
            return "=="
        elif (tmp == 6):
            return "!="
        elif (tmp == 7):
            return ">"
        elif (tmp == 8):
            return ">="
        elif (tmp == 9):
            return "<"
        elif (tmp == 10):
            return "<="
        elif (tmp == 11):
            return "&"
        elif (tmp == 12):
            return "|"
        elif (tmp == 13):
            return "^"
        elif (tmp == 14):
            return "&&"
        elif (tmp == 15):
            return "||"
        elif (tmp == 16):
            return "<<"
        elif (tmp == 17):
            return ">>"
        elif (tmp == 18):
            return ">>>"
        elif (tmp == 19):
            return "%"
        elif (tmp == 20):
            op1 = op.params[0]
            return (HxOverrides.stringOrNull(self.printBinop(op1)) + "=")
        elif (tmp == 21):
            return "..."
        elif (tmp == 22):
            return "=>"
        elif (tmp == 23):
            return "in"
        else:
            pass

    def escapeString(self,s,delim):
        return ((("null" if delim is None else delim) + HxOverrides.stringOrNull(StringTools.replace(StringTools.replace(StringTools.replace(StringTools.replace(StringTools.replace(StringTools.replace(s,"\n","\\n"),"\t","\\t"),"\r","\\r"),"'","\\'"),"\"","\\\""),"\x00","\\x00"))) + ("null" if delim is None else delim))

    def printFormatString(self,s):
        return self.escapeString(s,"'")

    def printString(self,s):
        return self.escapeString(s,"\"")

    def printConstant(self,c):
        tmp = c.index
        if (tmp == 0):
            s = c.params[0]
            return s
        elif (tmp == 1):
            s = c.params[0]
            return s
        elif (tmp == 2):
            _g = c.params[0]
            _g1 = c.params[1]
            if (_g1 is None):
                s = _g
                return self.printString(s)
            elif (_g1.index == 1):
                s = _g
                return self.printFormatString(s)
            else:
                s = _g
                return self.printString(s)
        elif (tmp == 3):
            s = c.params[0]
            return s
        elif (tmp == 4):
            s = c.params[0]
            opt = c.params[1]
            return ((("~/" + ("null" if s is None else s)) + "/") + ("null" if opt is None else opt))
        else:
            pass

    def printTypeParam(self,param):
        tmp = param.index
        if (tmp == 0):
            ct = param.params[0]
            return self.printComplexType(ct)
        elif (tmp == 1):
            e = param.params[0]
            return self.printExpr(e)
        else:
            pass

    def printTypePath(self,tp):
        tmp = None
        if (len(tp.pack) > 0):
            _this = tp.pack
            tmp = (HxOverrides.stringOrNull(".".join([python_Boot.toString1(x1,'') for x1 in _this])) + ".")
        else:
            tmp = ""
        tmp1 = ((("null" if tmp is None else tmp) + HxOverrides.stringOrNull(tp.name)) + HxOverrides.stringOrNull(((("." + HxOverrides.stringOrNull(Reflect.field(tp,"sub"))) if ((Reflect.field(tp,"sub") is not None)) else ""))))
        tmp = None
        if (Reflect.field(tp,"params") is None):
            tmp = ""
        elif (len(Reflect.field(tp,"params")) > 0):
            _this = list(map(self.printTypeParam,Reflect.field(tp,"params")))
            tmp = (("<" + HxOverrides.stringOrNull(", ".join([python_Boot.toString1(x1,'') for x1 in _this]))) + ">")
        else:
            tmp = ""
        return (("null" if tmp1 is None else tmp1) + ("null" if tmp is None else tmp))

    def printComplexType(self,ct):
        tmp = ct.index
        if (tmp == 0):
            tp = ct.params[0]
            return self.printTypePath(tp)
        elif (tmp == 1):
            args = ct.params[0]
            ret = ct.params[1]
            wrapArgumentsInParentheses = None
            if (len(args) == 1):
                _g = (args[0] if 0 < len(args) else None)
                wrapArgumentsInParentheses1 = _g.index
                if (wrapArgumentsInParentheses1 == 0):
                    _g1 = _g.params[0]
                    wrapArgumentsInParentheses = False
                elif (wrapArgumentsInParentheses1 == 3):
                    t = _g.params[0]
                    wrapArgumentsInParentheses = False
                elif (wrapArgumentsInParentheses1 == 5):
                    _g1 = _g.params[0]
                    if (_g1.index == 0):
                        _g = _g1.params[0]
                        wrapArgumentsInParentheses = False
                    else:
                        wrapArgumentsInParentheses = True
                else:
                    wrapArgumentsInParentheses = True
            else:
                wrapArgumentsInParentheses = True
            _this = list(map(self.printComplexType,args))
            argStr = ", ".join([python_Boot.toString1(x1,'') for x1 in _this])
            tmp = None
            if (ret.index == 1):
                _g = ret.params[0]
                _g = ret.params[1]
                tmp = (("(" + HxOverrides.stringOrNull(self.printComplexType(ret))) + ")")
            else:
                tmp = self.printComplexType(ret)
            return ((HxOverrides.stringOrNull((((("(" + ("null" if argStr is None else argStr)) + ")") if wrapArgumentsInParentheses else argStr))) + " -> ") + ("null" if tmp is None else tmp))
        elif (tmp == 2):
            fields = ct.params[0]
            _g = []
            _g1 = 0
            while (_g1 < len(fields)):
                f = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                _g1 = (_g1 + 1)
                x = (HxOverrides.stringOrNull(self.printField(f)) + "; ")
                _g.append(x)
            return (("{ " + HxOverrides.stringOrNull("".join([python_Boot.toString1(x1,'') for x1 in _g]))) + "}")
        elif (tmp == 3):
            ct1 = ct.params[0]
            return (("(" + HxOverrides.stringOrNull(self.printComplexType(ct1))) + ")")
        elif (tmp == 4):
            tpl = ct.params[0]
            fields = ct.params[1]
            _g = []
            _g1 = 0
            while (_g1 < len(tpl)):
                t = (tpl[_g1] if _g1 >= 0 and _g1 < len(tpl) else None)
                _g1 = (_g1 + 1)
                x = (("> " + HxOverrides.stringOrNull(self.printTypePath(t))) + ", ")
                _g.append(x)
            types = "".join([python_Boot.toString1(x1,'') for x1 in _g])
            _g = []
            _g1 = 0
            while (_g1 < len(fields)):
                f = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                _g1 = (_g1 + 1)
                x = (HxOverrides.stringOrNull(self.printField(f)) + "; ")
                _g.append(x)
            fields = "".join([python_Boot.toString1(x1,'') for x1 in _g])
            return ((("{" + ("null" if types is None else types)) + ("null" if fields is None else fields)) + "}")
        elif (tmp == 5):
            ct1 = ct.params[0]
            return ("?" + HxOverrides.stringOrNull(self.printComplexType(ct1)))
        elif (tmp == 6):
            n = ct.params[0]
            ct1 = ct.params[1]
            return ((("null" if n is None else n) + ":") + HxOverrides.stringOrNull(self.printComplexType(ct1)))
        elif (tmp == 7):
            tl = ct.params[0]
            _this = list(map(self.printComplexType,tl))
            return " & ".join([python_Boot.toString1(x1,'') for x1 in _this])
        else:
            pass

    def printMetadata(self,meta):
        return (("@" + HxOverrides.stringOrNull(meta.name)) + HxOverrides.stringOrNull((((("(" + HxOverrides.stringOrNull(self.printExprs(Reflect.field(meta,"params"),", "))) + ")") if (((Reflect.field(meta,"params") is not None) and ((len(Reflect.field(meta,"params")) > 0)))) else ""))))

    def printAccess(self,access):
        tmp = access.index
        if (tmp == 0):
            return "public"
        elif (tmp == 1):
            return "private"
        elif (tmp == 2):
            return "static"
        elif (tmp == 3):
            return "override"
        elif (tmp == 4):
            return "dynamic"
        elif (tmp == 5):
            return "inline"
        elif (tmp == 6):
            return "macro"
        elif (tmp == 7):
            return "final"
        elif (tmp == 8):
            return "extern"
        elif (tmp == 9):
            return "abstract"
        elif (tmp == 10):
            return "overload"
        else:
            pass

    def printField(self,field):
        tmp = (((((((("/**\n" + HxOverrides.stringOrNull(self.tabs)) + HxOverrides.stringOrNull(self.tabString)) + HxOverrides.stringOrNull(StringTools.replace(Reflect.field(field,"doc"),"\n",(("\n" + HxOverrides.stringOrNull(self.tabs)) + HxOverrides.stringOrNull(self.tabString))))) + "\n") + HxOverrides.stringOrNull(self.tabs)) + "**/\n") + HxOverrides.stringOrNull(self.tabs)) if (((Reflect.field(field,"doc") is not None) and ((Reflect.field(field,"doc") != "")))) else "")
        tmp1 = None
        if ((Reflect.field(field,"meta") is not None) and ((len(Reflect.field(field,"meta")) > 0))):
            _this = list(map(self.printMetadata,Reflect.field(field,"meta")))
            tmp1 = (HxOverrides.stringOrNull(("\n" + HxOverrides.stringOrNull(self.tabs)).join([python_Boot.toString1(x1,'') for x1 in _this])) + HxOverrides.stringOrNull((("\n" + HxOverrides.stringOrNull(self.tabs)))))
        else:
            tmp1 = ""
        tmp2 = None
        if ((Reflect.field(field,"access") is not None) and ((len(Reflect.field(field,"access")) > 0))):
            access = Reflect.field(field,"access")
            def _hx_local_2():
                def _hx_local_0(a):
                    return (a.index != 7)
                return (list(filter(_hx_local_0,access)) + [haxe_macro_Access.AFinal]) if Lambda.has(access,haxe_macro_Access.AFinal) else access
            _this = list(map(self.printAccess,_hx_local_2()))
            tmp2 = (HxOverrides.stringOrNull(" ".join([python_Boot.toString1(x1,'') for x1 in _this])) + " ")
        else:
            tmp2 = ""
        tmp3 = ((("null" if tmp is None else tmp) + ("null" if tmp1 is None else tmp1)) + ("null" if tmp2 is None else tmp2))
        _g = field.kind
        tmp = None
        tmp1 = _g.index
        if (tmp1 == 0):
            t = _g.params[0]
            eo = _g.params[1]
            tmp = (((HxOverrides.stringOrNull((("" if (((Reflect.field(field,"access") is not None) and Lambda.has(Reflect.field(field,"access"),haxe_macro_Access.AFinal))) else "var "))) + HxOverrides.stringOrNull((("" + HxOverrides.stringOrNull(field.name))))) + HxOverrides.stringOrNull(self.opt(t,self.printComplexType," : "))) + HxOverrides.stringOrNull(self.opt(eo,self.printExpr," = ")))
        elif (tmp1 == 1):
            func = _g.params[0]
            tmp = (("function " + HxOverrides.stringOrNull(field.name)) + HxOverrides.stringOrNull(self.printFunction(func)))
        elif (tmp1 == 2):
            get = _g.params[0]
            _hx_set = _g.params[1]
            t = _g.params[2]
            eo = _g.params[3]
            tmp = (((((((("var " + HxOverrides.stringOrNull(field.name)) + "(") + ("null" if get is None else get)) + ", ") + ("null" if _hx_set is None else _hx_set)) + ")") + HxOverrides.stringOrNull(self.opt(t,self.printComplexType," : "))) + HxOverrides.stringOrNull(self.opt(eo,self.printExpr," = ")))
        else:
            pass
        return (("null" if tmp3 is None else tmp3) + ("null" if tmp is None else tmp))

    def printTypeParamDecl(self,tpd):
        tmp = None
        if ((Reflect.field(tpd,"meta") is not None) and ((len(Reflect.field(tpd,"meta")) > 0))):
            _this = list(map(self.printMetadata,Reflect.field(tpd,"meta")))
            tmp = (HxOverrides.stringOrNull(" ".join([python_Boot.toString1(x1,'') for x1 in _this])) + " ")
        else:
            tmp = ""
        tmp1 = (("null" if tmp is None else tmp) + HxOverrides.stringOrNull(tpd.name))
        tmp = None
        if ((Reflect.field(tpd,"params") is not None) and ((len(Reflect.field(tpd,"params")) > 0))):
            _this = list(map(self.printTypeParamDecl,Reflect.field(tpd,"params")))
            tmp = (("<" + HxOverrides.stringOrNull(", ".join([python_Boot.toString1(x1,'') for x1 in _this]))) + ">")
        else:
            tmp = ""
        tmp2 = None
        if ((Reflect.field(tpd,"constraints") is not None) and ((len(Reflect.field(tpd,"constraints")) > 0))):
            _this = list(map(self.printComplexType,Reflect.field(tpd,"constraints")))
            tmp2 = ((":(" + HxOverrides.stringOrNull(", ".join([python_Boot.toString1(x1,'') for x1 in _this]))) + ")")
        else:
            tmp2 = ""
        return ((("null" if tmp1 is None else tmp1) + ("null" if tmp is None else tmp)) + ("null" if tmp2 is None else tmp2))

    def printFunctionArg(self,arg):
        return (((HxOverrides.stringOrNull((("?" if (Reflect.field(arg,"opt")) else ""))) + HxOverrides.stringOrNull(arg.name)) + HxOverrides.stringOrNull(self.opt(Reflect.field(arg,"type"),self.printComplexType,":"))) + HxOverrides.stringOrNull(self.opt(Reflect.field(arg,"value"),self.printExpr," = ")))

    def printFunction(self,func,kind = None):
        skipParentheses = None
        _g = func.args
        if (len(_g) == 1):
            _g1 = (_g[0] if 0 < len(_g) else None)
            _g = Reflect.field(_g1,"meta")
            _g = _g1.name
            _g = Reflect.field(_g1,"opt")
            _g = Reflect.field(_g1,"value")
            skipParentheses = ((Reflect.field(_g1,"type") is None) and ((kind == haxe_macro_FunctionKind.FArrow)))
        else:
            skipParentheses = False
        tmp = None
        if (Reflect.field(func,"params") is None):
            tmp = ""
        elif (len(Reflect.field(func,"params")) > 0):
            _this = list(map(self.printTypeParamDecl,Reflect.field(func,"params")))
            tmp = (("<" + HxOverrides.stringOrNull(", ".join([python_Boot.toString1(x1,'') for x1 in _this]))) + ">")
        else:
            tmp = ""
        _this = list(map(self.printFunctionArg,func.args))
        return ((((((("null" if tmp is None else tmp) + HxOverrides.stringOrNull((("" if skipParentheses else "(")))) + HxOverrides.stringOrNull(", ".join([python_Boot.toString1(x1,'') for x1 in _this]))) + HxOverrides.stringOrNull((("" if skipParentheses else ")")))) + HxOverrides.stringOrNull(((" ->" if ((kind == haxe_macro_FunctionKind.FArrow)) else "")))) + HxOverrides.stringOrNull(self.opt(Reflect.field(func,"ret"),self.printComplexType,":"))) + HxOverrides.stringOrNull(self.opt(Reflect.field(func,"expr"),self.printExpr," ")))

    def printVar(self,v):
        s = ((HxOverrides.stringOrNull(v.name) + HxOverrides.stringOrNull(self.opt(Reflect.field(v,"type"),self.printComplexType,":"))) + HxOverrides.stringOrNull(self.opt(Reflect.field(v,"expr"),self.printExpr," = ")))
        _g = Reflect.field(v,"meta")
        if (_g is None):
            return s
        elif (len(_g) == 0):
            return s
        else:
            meta = _g
            _this = list(map(self.printMetadata,meta))
            return ((HxOverrides.stringOrNull(" ".join([python_Boot.toString1(x1,'') for x1 in _this])) + " ") + ("null" if s is None else s))

    def printObjectFieldKey(self,of):
        _g = Reflect.field(of,"quotes")
        if (_g is None):
            return of.field
        else:
            tmp = _g.index
            if (tmp == 0):
                return of.field
            elif (tmp == 1):
                return (("\"" + HxOverrides.stringOrNull(of.field)) + "\"")
            else:
                pass

    def printObjectField(self,of):
        return ((("" + HxOverrides.stringOrNull(self.printObjectFieldKey(of))) + " : ") + HxOverrides.stringOrNull(self.printExpr(of.expr)))

    def printExpr(self,e):
        _gthis = self
        if (e is None):
            return "#NULL"
        else:
            _g = e.expr
            tmp = _g.index
            if (tmp == 0):
                c = _g.params[0]
                return self.printConstant(c)
            elif (tmp == 1):
                e1 = _g.params[0]
                e2 = _g.params[1]
                return (((("" + HxOverrides.stringOrNull(self.printExpr(e1))) + "[") + HxOverrides.stringOrNull(self.printExpr(e2))) + "]")
            elif (tmp == 2):
                op = _g.params[0]
                e1 = _g.params[1]
                e2 = _g.params[2]
                return ((((("" + HxOverrides.stringOrNull(self.printExpr(e1))) + " ") + HxOverrides.stringOrNull(self.printBinop(op))) + " ") + HxOverrides.stringOrNull(self.printExpr(e2)))
            elif (tmp == 3):
                e1 = _g.params[0]
                n = _g.params[1]
                return ((("" + HxOverrides.stringOrNull(self.printExpr(e1))) + ".") + ("null" if n is None else n))
            elif (tmp == 4):
                e1 = _g.params[0]
                return (("(" + HxOverrides.stringOrNull(self.printExpr(e1))) + ")")
            elif (tmp == 5):
                fl = _g.params[0]
                def _hx_local_0(fld):
                    return _gthis.printObjectField(fld)
                _this = list(map(_hx_local_0,fl))
                return (("{ " + HxOverrides.stringOrNull(", ".join([python_Boot.toString1(x1,'') for x1 in _this]))) + " }")
            elif (tmp == 6):
                el = _g.params[0]
                return (("[" + HxOverrides.stringOrNull(self.printExprs(el,", "))) + "]")
            elif (tmp == 7):
                e1 = _g.params[0]
                el = _g.params[1]
                return (((("" + HxOverrides.stringOrNull(self.printExpr(e1))) + "(") + HxOverrides.stringOrNull(self.printExprs(el,", "))) + ")")
            elif (tmp == 8):
                tp = _g.params[0]
                el = _g.params[1]
                return (((("new " + HxOverrides.stringOrNull(self.printTypePath(tp))) + "(") + HxOverrides.stringOrNull(self.printExprs(el,", "))) + ")")
            elif (tmp == 9):
                _g1 = _g.params[0]
                _g2 = _g.params[2]
                if _g.params[1]:
                    op = _g1
                    e1 = _g2
                    return (HxOverrides.stringOrNull(self.printExpr(e1)) + HxOverrides.stringOrNull(self.printUnop(op)))
                else:
                    op = _g1
                    e1 = _g2
                    return (HxOverrides.stringOrNull(self.printUnop(op)) + HxOverrides.stringOrNull(self.printExpr(e1)))
            elif (tmp == 10):
                vl = _g.params[0]
                _this = list(map(self.printVar,vl))
                return ("var " + HxOverrides.stringOrNull(", ".join([python_Boot.toString1(x1,'') for x1 in _this])))
            elif (tmp == 11):
                _g1 = _g.params[0]
                _g2 = _g.params[1]
                if (_g1 is None):
                    kind = _g1
                    func = _g2
                    return (HxOverrides.stringOrNull((("function" if ((kind != haxe_macro_FunctionKind.FArrow)) else ""))) + HxOverrides.stringOrNull(self.printFunction(func,kind)))
                elif (_g1.index == 1):
                    no = _g1.params[0]
                    inlined = _g1.params[1]
                    func = _g2
                    return ((HxOverrides.stringOrNull((("inline " if inlined else ""))) + HxOverrides.stringOrNull((("function " + ("null" if no is None else no))))) + HxOverrides.stringOrNull(self.printFunction(func)))
                else:
                    kind = _g1
                    func = _g2
                    return (HxOverrides.stringOrNull((("function" if ((kind != haxe_macro_FunctionKind.FArrow)) else ""))) + HxOverrides.stringOrNull(self.printFunction(func,kind)))
            elif (tmp == 12):
                _g1 = _g.params[0]
                if (len(_g1) == 0):
                    return "{ }"
                else:
                    el = _g1
                    old = self.tabs
                    _hx_local_1 = self
                    _hx_local_2 = _hx_local_1.tabs
                    _hx_local_1.tabs = (("null" if _hx_local_2 is None else _hx_local_2) + HxOverrides.stringOrNull(self.tabString))
                    _hx_local_1.tabs
                    s = (("{\n" + HxOverrides.stringOrNull(self.tabs)) + HxOverrides.stringOrNull(self.printExprs(el,(";\n" + HxOverrides.stringOrNull(self.tabs)))))
                    self.tabs = old
                    return (("null" if s is None else s) + HxOverrides.stringOrNull((((";\n" + HxOverrides.stringOrNull(self.tabs)) + "}"))))
            elif (tmp == 13):
                e1 = _g.params[0]
                e2 = _g.params[1]
                return ((("for (" + HxOverrides.stringOrNull(self.printExpr(e1))) + ") ") + HxOverrides.stringOrNull(self.printExpr(e2)))
            elif (tmp == 14):
                _g1 = _g.params[0]
                _g2 = _g.params[1]
                _g3 = _g.params[2]
                if (_g3 is None):
                    eif = _g2
                    econd = _g1
                    return ((("if (" + HxOverrides.stringOrNull(self.printExpr(econd))) + ") ") + HxOverrides.stringOrNull(self.printExpr(eif)))
                else:
                    eelse = _g3
                    eif = _g2
                    econd = _g1
                    return ((((("if (" + HxOverrides.stringOrNull(self.printExpr(econd))) + ") ") + HxOverrides.stringOrNull(self.printExpr(eif))) + " else ") + HxOverrides.stringOrNull(self.printExpr(eelse)))
            elif (tmp == 15):
                _g1 = _g.params[0]
                _g2 = _g.params[1]
                if _g.params[2]:
                    e1 = _g2
                    econd = _g1
                    return ((("while (" + HxOverrides.stringOrNull(self.printExpr(econd))) + ") ") + HxOverrides.stringOrNull(self.printExpr(e1)))
                else:
                    e1 = _g2
                    econd = _g1
                    return (((("do " + HxOverrides.stringOrNull(self.printExpr(e1))) + " while (") + HxOverrides.stringOrNull(self.printExpr(econd))) + ")")
            elif (tmp == 16):
                e1 = _g.params[0]
                cl = _g.params[1]
                edef = _g.params[2]
                old = self.tabs
                _hx_local_3 = self
                _hx_local_4 = _hx_local_3.tabs
                _hx_local_3.tabs = (("null" if _hx_local_4 is None else _hx_local_4) + HxOverrides.stringOrNull(self.tabString))
                _hx_local_3.tabs
                s = ((("switch " + HxOverrides.stringOrNull(self.printExpr(e1))) + " {\n") + HxOverrides.stringOrNull(self.tabs))
                def _hx_local_5(c):
                    return ((("case " + HxOverrides.stringOrNull(_gthis.printExprs(c.values,", "))) + HxOverrides.stringOrNull(((((" if (" + HxOverrides.stringOrNull(_gthis.printExpr(Reflect.field(c,"guard")))) + "):") if ((Reflect.field(c,"guard") is not None)) else ":")))) + HxOverrides.stringOrNull((((HxOverrides.stringOrNull(_gthis.opt(Reflect.field(c,"expr"),_gthis.printExpr)) + ";") if ((Reflect.field(c,"expr") is not None)) else ""))))
                _this = list(map(_hx_local_5,cl))
                s1 = (("null" if s is None else s) + HxOverrides.stringOrNull(("\n" + HxOverrides.stringOrNull(self.tabs)).join([python_Boot.toString1(x1,'') for x1 in _this])))
                if (edef is not None):
                    s1 = (("null" if s1 is None else s1) + HxOverrides.stringOrNull((((("\n" + HxOverrides.stringOrNull(self.tabs)) + "default:") + HxOverrides.stringOrNull((("" if ((edef.expr is None)) else (HxOverrides.stringOrNull(self.printExpr(edef)) + ";"))))))))
                self.tabs = old
                return (("null" if s1 is None else s1) + HxOverrides.stringOrNull(((("\n" + HxOverrides.stringOrNull(self.tabs)) + "}"))))
            elif (tmp == 17):
                e1 = _g.params[0]
                cl = _g.params[1]
                tmp = ("try " + HxOverrides.stringOrNull(self.printExpr(e1)))
                def _hx_local_7(c):
                    return ((((" catch(" + HxOverrides.stringOrNull(c.name)) + HxOverrides.stringOrNull((("" if ((Reflect.field(c,"type") is None)) else (":" + HxOverrides.stringOrNull(_gthis.printComplexType(Reflect.field(c,"type")))))))) + ") ") + HxOverrides.stringOrNull(_gthis.printExpr(c.expr)))
                _this = list(map(_hx_local_7,cl))
                return (("null" if tmp is None else tmp) + HxOverrides.stringOrNull("".join([python_Boot.toString1(x1,'') for x1 in _this])))
            elif (tmp == 18):
                eo = _g.params[0]
                return ("return" + HxOverrides.stringOrNull(self.opt(eo,self.printExpr," ")))
            elif (tmp == 19):
                return "break"
            elif (tmp == 20):
                return "continue"
            elif (tmp == 21):
                e1 = _g.params[0]
                return ("untyped " + HxOverrides.stringOrNull(self.printExpr(e1)))
            elif (tmp == 22):
                e1 = _g.params[0]
                return ("throw " + HxOverrides.stringOrNull(self.printExpr(e1)))
            elif (tmp == 23):
                _g1 = _g.params[0]
                e1 = _g1
                cto = _g.params[1]
                if (cto is not None):
                    return (((("cast(" + HxOverrides.stringOrNull(self.printExpr(e1))) + ", ") + HxOverrides.stringOrNull(self.printComplexType(cto))) + ")")
                else:
                    e1 = _g1
                    return ("cast " + HxOverrides.stringOrNull(self.printExpr(e1)))
            elif (tmp == 24):
                _g1 = _g.params[1]
                e1 = _g.params[0]
                return (("#DISPLAY(" + HxOverrides.stringOrNull(self.printExpr(e1))) + ")")
            elif (tmp == 25):
                tp = _g.params[0]
                return (("#DISPLAY(" + HxOverrides.stringOrNull(self.printTypePath(tp))) + ")")
            elif (tmp == 26):
                econd = _g.params[0]
                eif = _g.params[1]
                eelse = _g.params[2]
                return ((((("" + HxOverrides.stringOrNull(self.printExpr(econd))) + " ? ") + HxOverrides.stringOrNull(self.printExpr(eif))) + " : ") + HxOverrides.stringOrNull(self.printExpr(eelse)))
            elif (tmp == 27):
                e1 = _g.params[0]
                ct = _g.params[1]
                return (((("(" + HxOverrides.stringOrNull(self.printExpr(e1))) + " : ") + HxOverrides.stringOrNull(self.printComplexType(ct))) + ")")
            elif (tmp == 28):
                _g1 = _g.params[0]
                _g2 = _g.params[1]
                _g3 = Reflect.field(_g1,"params")
                _g3 = _g1.pos
                if (_g1.name == ":implicitReturn"):
                    _g3 = _g2.expr
                    _g4 = _g2.pos
                    if (_g3.index == 18):
                        e1 = _g3.params[0]
                        return self.printExpr(e1)
                    else:
                        meta = _g1
                        e1 = _g2
                        return ((HxOverrides.stringOrNull(self.printMetadata(meta)) + " ") + HxOverrides.stringOrNull(self.printExpr(e1)))
                else:
                    meta = _g1
                    e1 = _g2
                    return ((HxOverrides.stringOrNull(self.printMetadata(meta)) + " ") + HxOverrides.stringOrNull(self.printExpr(e1)))
            elif (tmp == 29):
                e1 = _g.params[0]
                ct = _g.params[1]
                return ((("" + HxOverrides.stringOrNull(self.printExpr(e1))) + " is ") + HxOverrides.stringOrNull(self.printComplexType(ct)))
            else:
                pass

    def printExprs(self,el,sep):
        _this = list(map(self.printExpr,el))
        return sep.join([python_Boot.toString1(x1,'') for x1 in _this])

    def printExtension(self,tpl,fields):
        tmp = (("{\n" + HxOverrides.stringOrNull(self.tabs)) + ">")
        _this = list(map(self.printTypePath,tpl))
        tmp1 = ((("null" if tmp is None else tmp) + HxOverrides.stringOrNull(((",\n" + HxOverrides.stringOrNull(self.tabs)) + ">").join([python_Boot.toString1(x1,'') for x1 in _this]))) + ",")
        tmp = None
        if (len(fields) > 0):
            tmp2 = ("\n" + HxOverrides.stringOrNull(self.tabs))
            _this = list(map(self.printField,fields))
            tmp = ((("null" if tmp2 is None else tmp2) + HxOverrides.stringOrNull((";\n" + HxOverrides.stringOrNull(self.tabs)).join([python_Boot.toString1(x1,'') for x1 in _this]))) + ";\n}")
        else:
            tmp = "\n}"
        return (("null" if tmp1 is None else tmp1) + ("null" if tmp is None else tmp))

    def printStructure(self,fields):
        if (len(fields) == 0):
            return "{ }"
        else:
            tmp = ("{\n" + HxOverrides.stringOrNull(self.tabs))
            _this = list(map(self.printField,fields))
            return ((("null" if tmp is None else tmp) + HxOverrides.stringOrNull((";\n" + HxOverrides.stringOrNull(self.tabs)).join([python_Boot.toString1(x1,'') for x1 in _this]))) + ";\n}")

    def printTypeDefinition(self,t,printPackage = None):
        if (printPackage is None):
            printPackage = True
        old = self.tabs
        self.tabs = self.tabString
        _hx_str = None
        if (t is None):
            _hx_str = "#NULL"
        else:
            str1 = None
            if ((printPackage and ((len(t.pack) > 0))) and (((t.pack[0] if 0 < len(t.pack) else None) != ""))):
                _this = t.pack
                str1 = (("package " + HxOverrides.stringOrNull(".".join([python_Boot.toString1(x1,'') for x1 in _this]))) + ";\n")
            else:
                str1 = ""
            str2 = (((("/**\n" + HxOverrides.stringOrNull(self.tabString)) + HxOverrides.stringOrNull(StringTools.replace(Reflect.field(t,"doc"),"\n",("\n" + HxOverrides.stringOrNull(self.tabString))))) + "\n**/\n") if (((Reflect.field(t,"doc") is not None) and ((Reflect.field(t,"doc") != "")))) else "")
            str3 = None
            if ((Reflect.field(t,"meta") is not None) and ((len(Reflect.field(t,"meta")) > 0))):
                _this = list(map(self.printMetadata,Reflect.field(t,"meta")))
                str3 = (HxOverrides.stringOrNull(" ".join([python_Boot.toString1(x1,'') for x1 in _this])) + " ")
            else:
                str3 = ""
            str4 = (((("null" if str1 is None else str1) + ("null" if str2 is None else str2)) + ("null" if str3 is None else str3)) + HxOverrides.stringOrNull((("extern " if (Reflect.field(t,"isExtern")) else ""))))
            _g = t.kind
            str1 = None
            str2 = _g.index
            if (str2 == 0):
                str2 = ("enum " + HxOverrides.stringOrNull(t.name))
                str3 = None
                if ((Reflect.field(t,"params") is not None) and ((len(Reflect.field(t,"params")) > 0))):
                    _this = list(map(self.printTypeParamDecl,Reflect.field(t,"params")))
                    str3 = (("<" + HxOverrides.stringOrNull(", ".join([python_Boot.toString1(x1,'') for x1 in _this]))) + ">")
                else:
                    str3 = ""
                str5 = ((("null" if str2 is None else str2) + ("null" if str3 is None else str3)) + " {\n")
                _g1 = []
                _g2 = 0
                _g3 = t.fields
                while (_g2 < len(_g3)):
                    field = (_g3[_g2] if _g2 >= 0 and _g2 < len(_g3) else None)
                    _g2 = (_g2 + 1)
                    x = self.tabs
                    x1 = (((((((("/**\n" + HxOverrides.stringOrNull(self.tabs)) + HxOverrides.stringOrNull(self.tabString)) + HxOverrides.stringOrNull(StringTools.replace(Reflect.field(field,"doc"),"\n",(("\n" + HxOverrides.stringOrNull(self.tabs)) + HxOverrides.stringOrNull(self.tabString))))) + "\n") + HxOverrides.stringOrNull(self.tabs)) + "**/\n") + HxOverrides.stringOrNull(self.tabs)) if (((Reflect.field(field,"doc") is not None) and ((Reflect.field(field,"doc") != "")))) else "")
                    x2 = None
                    if ((Reflect.field(field,"meta") is not None) and ((len(Reflect.field(field,"meta")) > 0))):
                        _this = list(map(self.printMetadata,Reflect.field(field,"meta")))
                        x2 = (HxOverrides.stringOrNull(" ".join([python_Boot.toString1(x1,'') for x1 in _this])) + " ")
                    else:
                        x2 = ""
                    x3 = ((("null" if x is None else x) + ("null" if x1 is None else x1)) + ("null" if x2 is None else x2))
                    _g4 = field.kind
                    x4 = None
                    x5 = _g4.index
                    if (x5 == 0):
                        _g5 = _g4.params[1]
                        t1 = _g4.params[0]
                        x4 = (HxOverrides.stringOrNull(field.name) + HxOverrides.stringOrNull(self.opt(t1,self.printComplexType,":")))
                    elif (x5 == 1):
                        func = _g4.params[0]
                        x4 = (HxOverrides.stringOrNull(field.name) + HxOverrides.stringOrNull(self.printFunction(func)))
                    elif (x5 == 2):
                        _g6 = _g4.params[0]
                        _g7 = _g4.params[1]
                        _g8 = _g4.params[2]
                        _g9 = _g4.params[3]
                        raise haxe_Exception.thrown("FProp is invalid for TDEnum.")
                    else:
                        pass
                    _g1.append(((("null" if x3 is None else x3) + ("null" if x4 is None else x4)) + ";"))
                str1 = ((("null" if str5 is None else str5) + HxOverrides.stringOrNull("\n".join([python_Boot.toString1(x1,'') for x1 in _g1]))) + "\n}")
            elif (str2 == 1):
                str2 = ("typedef " + HxOverrides.stringOrNull(t.name))
                str3 = None
                if ((Reflect.field(t,"params") is not None) and ((len(Reflect.field(t,"params")) > 0))):
                    _this = list(map(self.printTypeParamDecl,Reflect.field(t,"params")))
                    str3 = (("<" + HxOverrides.stringOrNull(", ".join([python_Boot.toString1(x1,'') for x1 in _this]))) + ">")
                else:
                    str3 = ""
                str5 = ((("null" if str2 is None else str2) + ("null" if str3 is None else str3)) + " = {\n")
                _g1 = []
                _g2 = 0
                _g3 = t.fields
                while (_g2 < len(_g3)):
                    f = (_g3[_g2] if _g2 >= 0 and _g2 < len(_g3) else None)
                    _g2 = (_g2 + 1)
                    x = ((HxOverrides.stringOrNull(self.tabs) + HxOverrides.stringOrNull(self.printField(f))) + ";")
                    _g1.append(x)
                str1 = ((("null" if str5 is None else str5) + HxOverrides.stringOrNull("\n".join([python_Boot.toString1(x1,'') for x1 in _g1]))) + "\n}")
            elif (str2 == 2):
                superClass = _g.params[0]
                interfaces = _g.params[1]
                isInterface = _g.params[2]
                isFinal = _g.params[3]
                isAbstract = _g.params[4]
                str2 = (((HxOverrides.stringOrNull((("final " if isFinal else ""))) + HxOverrides.stringOrNull((("abstract " if isAbstract else "")))) + HxOverrides.stringOrNull((("interface " if isInterface else "class ")))) + HxOverrides.stringOrNull(t.name))
                str3 = None
                if ((Reflect.field(t,"params") is not None) and ((len(Reflect.field(t,"params")) > 0))):
                    _this = list(map(self.printTypeParamDecl,Reflect.field(t,"params")))
                    str3 = (("<" + HxOverrides.stringOrNull(", ".join([python_Boot.toString1(x1,'') for x1 in _this]))) + ">")
                else:
                    str3 = ""
                str5 = ((("null" if str2 is None else str2) + ("null" if str3 is None else str3)) + HxOverrides.stringOrNull((((" extends " + HxOverrides.stringOrNull(self.printTypePath(superClass))) if ((superClass is not None)) else ""))))
                str2 = None
                if (interfaces is not None):
                    _this = None
                    if isInterface:
                        _g1 = []
                        _g2 = 0
                        while (_g2 < len(interfaces)):
                            tp = (interfaces[_g2] if _g2 >= 0 and _g2 < len(interfaces) else None)
                            _g2 = (_g2 + 1)
                            x = (" extends " + HxOverrides.stringOrNull(self.printTypePath(tp)))
                            _g1.append(x)
                        _this = _g1
                    else:
                        _g1 = []
                        _g2 = 0
                        while (_g2 < len(interfaces)):
                            tp = (interfaces[_g2] if _g2 >= 0 and _g2 < len(interfaces) else None)
                            _g2 = (_g2 + 1)
                            x = (" implements " + HxOverrides.stringOrNull(self.printTypePath(tp)))
                            _g1.append(x)
                        _this = _g1
                    str2 = "".join([python_Boot.toString1(x1,'') for x1 in _this])
                else:
                    str2 = ""
                str3 = ((("null" if str5 is None else str5) + ("null" if str2 is None else str2)) + " {\n")
                _g1 = []
                _g2 = 0
                _g3 = t.fields
                while (_g2 < len(_g3)):
                    f = (_g3[_g2] if _g2 >= 0 and _g2 < len(_g3) else None)
                    _g2 = (_g2 + 1)
                    x = (HxOverrides.stringOrNull(self.tabs) + HxOverrides.stringOrNull(self.printFieldWithDelimiter(f)))
                    _g1.append(x)
                str1 = ((("null" if str3 is None else str3) + HxOverrides.stringOrNull("\n".join([python_Boot.toString1(x1,'') for x1 in _g1]))) + "\n}")
            elif (str2 == 3):
                ct = _g.params[0]
                str2 = ("typedef " + HxOverrides.stringOrNull(t.name))
                str3 = None
                if ((Reflect.field(t,"params") is not None) and ((len(Reflect.field(t,"params")) > 0))):
                    _this = list(map(self.printTypeParamDecl,Reflect.field(t,"params")))
                    str3 = (("<" + HxOverrides.stringOrNull(", ".join([python_Boot.toString1(x1,'') for x1 in _this]))) + ">")
                else:
                    str3 = ""
                str5 = ((("null" if str2 is None else str2) + ("null" if str3 is None else str3)) + " = ")
                str2 = None
                str3 = ct.index
                if (str3 == 2):
                    fields = ct.params[0]
                    str2 = self.printStructure(fields)
                elif (str3 == 4):
                    tpl = ct.params[0]
                    fields = ct.params[1]
                    str2 = self.printExtension(tpl,fields)
                else:
                    str2 = self.printComplexType(ct)
                str1 = ((("null" if str5 is None else str5) + ("null" if str2 is None else str2)) + ";")
            elif (str2 == 4):
                tthis = _g.params[0]
                _hx_from = _g.params[1]
                to = _g.params[2]
                str2 = ("abstract " + HxOverrides.stringOrNull(t.name))
                str3 = None
                if ((Reflect.field(t,"params") is not None) and ((len(Reflect.field(t,"params")) > 0))):
                    _this = list(map(self.printTypeParamDecl,Reflect.field(t,"params")))
                    str3 = (("<" + HxOverrides.stringOrNull(", ".join([python_Boot.toString1(x1,'') for x1 in _this]))) + ">")
                else:
                    str3 = ""
                str5 = ((("null" if str2 is None else str2) + ("null" if str3 is None else str3)) + HxOverrides.stringOrNull((("" if ((tthis is None)) else (("(" + HxOverrides.stringOrNull(self.printComplexType(tthis))) + ")")))))
                str2 = None
                if (_hx_from is None):
                    str2 = ""
                else:
                    _g1 = []
                    _g2 = 0
                    while (_g2 < len(_hx_from)):
                        f = (_hx_from[_g2] if _g2 >= 0 and _g2 < len(_hx_from) else None)
                        _g2 = (_g2 + 1)
                        x = (" from " + HxOverrides.stringOrNull(self.printComplexType(f)))
                        _g1.append(x)
                    str2 = "".join([python_Boot.toString1(x1,'') for x1 in _g1])
                str3 = (("null" if str5 is None else str5) + ("null" if str2 is None else str2))
                str2 = None
                if (to is None):
                    str2 = ""
                else:
                    _g1 = []
                    _g2 = 0
                    while (_g2 < len(to)):
                        t1 = (to[_g2] if _g2 >= 0 and _g2 < len(to) else None)
                        _g2 = (_g2 + 1)
                        x = (" to " + HxOverrides.stringOrNull(self.printComplexType(t1)))
                        _g1.append(x)
                    str2 = "".join([python_Boot.toString1(x1,'') for x1 in _g1])
                str5 = ((("null" if str3 is None else str3) + ("null" if str2 is None else str2)) + " {\n")
                _g1 = []
                _g2 = 0
                _g3 = t.fields
                while (_g2 < len(_g3)):
                    f = (_g3[_g2] if _g2 >= 0 and _g2 < len(_g3) else None)
                    _g2 = (_g2 + 1)
                    x = (HxOverrides.stringOrNull(self.tabs) + HxOverrides.stringOrNull(self.printFieldWithDelimiter(f)))
                    _g1.append(x)
                str1 = ((("null" if str5 is None else str5) + HxOverrides.stringOrNull("\n".join([python_Boot.toString1(x1,'') for x1 in _g1]))) + "\n}")
            elif (str2 == 5):
                kind = _g.params[0]
                access = _g.params[1]
                self.tabs = old
                str2 = None
                if ((access is not None) and ((len(access) > 0))):
                    _this = list(map(self.printAccess,access))
                    str2 = (HxOverrides.stringOrNull(" ".join([python_Boot.toString1(x1,'') for x1 in _this])) + " ")
                else:
                    str2 = ""
                str3 = None
                str5 = kind.index
                if (str5 == 0):
                    _hx_type = kind.params[0]
                    eo = kind.params[1]
                    str3 = ((((HxOverrides.stringOrNull((("" if (((access is not None) and Lambda.has(access,haxe_macro_Access.AFinal))) else "var "))) + HxOverrides.stringOrNull((("" + HxOverrides.stringOrNull(t.name))))) + HxOverrides.stringOrNull(self.opt(_hx_type,self.printComplexType," : "))) + HxOverrides.stringOrNull(self.opt(eo,self.printExpr," = "))) + ";")
                elif (str5 == 1):
                    func = kind.params[0]
                    str5 = (("function " + HxOverrides.stringOrNull(t.name)) + HxOverrides.stringOrNull(self.printFunction(func)))
                    _g = Reflect.field(func,"expr")
                    str6 = None
                    if (_g is None):
                        str6 = ";"
                    else:
                        _g1 = _g.expr
                        _g2 = _g.pos
                        if (_g1.index == 12):
                            _g = _g1.params[0]
                            str6 = ""
                        else:
                            str6 = ";"
                    str3 = (("null" if str5 is None else str5) + ("null" if str6 is None else str6))
                elif (str5 == 2):
                    get = kind.params[0]
                    _hx_set = kind.params[1]
                    _hx_type = kind.params[2]
                    eo = kind.params[3]
                    str3 = ((((((((("var " + HxOverrides.stringOrNull(t.name)) + "(") + ("null" if get is None else get)) + ", ") + ("null" if _hx_set is None else _hx_set)) + ")") + HxOverrides.stringOrNull(self.opt(_hx_type,self.printComplexType," : "))) + HxOverrides.stringOrNull(self.opt(eo,self.printExpr," = "))) + ";")
                else:
                    pass
                str1 = (("null" if str2 is None else str2) + ("null" if str3 is None else str3))
            else:
                pass
            _hx_str = (("null" if str4 is None else str4) + ("null" if str1 is None else str1))
        self.tabs = old
        return _hx_str

    def printFieldWithDelimiter(self,f):
        tmp = self.printField(f)
        _g = f.kind
        tmp1 = None
        tmp2 = _g.index
        if (tmp2 == 0):
            _g1 = _g.params[0]
            _g1 = _g.params[1]
            tmp1 = ";"
        elif (tmp2 == 1):
            _g1 = _g.params[0]
            _g2 = _g1.args
            _g2 = Reflect.field(_g1,"expr")
            _g3 = Reflect.field(_g1,"params")
            _g3 = Reflect.field(_g1,"ret")
            if (_g2 is None):
                tmp1 = ";"
            else:
                _g1 = _g2.expr
                _g3 = _g2.pos
                if (_g1.index == 12):
                    _g2 = _g1.params[0]
                    tmp1 = ""
                else:
                    tmp1 = ";"
        elif (tmp2 == 2):
            _g1 = _g.params[0]
            _g1 = _g.params[1]
            _g1 = _g.params[2]
            _g1 = _g.params[3]
            tmp1 = ";"
        else:
            pass
        return (("null" if tmp is None else tmp) + ("null" if tmp1 is None else tmp1))

    def opt(self,v,f,prefix = None):
        if (prefix is None):
            prefix = ""
        if (v is None):
            return ""
        else:
            return (("null" if prefix is None else prefix) + HxOverrides.stringOrNull(f(v)))

    def printExprWithPositions(self,e):
        _gthis = self
        buffer_b = python_lib_io_StringIO()
        def _hx_local_0(i):
            return StringTools.lpad(Std.string(i)," ",4)
        format4 = _hx_local_0
        loop = None
        def _hx_local_8(tabs,e):
            def _hx_local_1(s,p = None):
                if (p is None):
                    p = e.pos
                p = e.pos
                s1 = Std.string(((((((("" + HxOverrides.stringOrNull(format4(p.min))) + "-") + HxOverrides.stringOrNull(format4(p.max))) + " ") + ("null" if tabs is None else tabs)) + ("null" if s is None else s)) + "\n"))
                buffer_b.write(s1)
            add = _hx_local_1
            def _hx_local_2(e):
                loop((("null" if tabs is None else tabs) + HxOverrides.stringOrNull(_gthis.tabString)),e)
            loopI = _hx_local_2
            _g = e.expr
            loop1 = _g.index
            if (loop1 == 0):
                c = _g.params[0]
                add(_gthis.printConstant(c))
            elif (loop1 == 1):
                e1 = _g.params[0]
                e2 = _g.params[1]
                add("EArray")
                loopI(e1)
                loopI(e2)
            elif (loop1 == 2):
                op = _g.params[0]
                e1 = _g.params[1]
                e2 = _g.params[2]
                add(("EBinop " + HxOverrides.stringOrNull(_gthis.printBinop(op))))
                loopI(e1)
                loopI(e2)
            elif (loop1 == 3):
                e1 = _g.params[0]
                field = _g.params[1]
                add(("EField " + ("null" if field is None else field)))
                loopI(e1)
            elif (loop1 == 4):
                e1 = _g.params[0]
                add("EParenthesis")
                loopI(e1)
            elif (loop1 == 5):
                fields = _g.params[0]
                add("EObjectDecl")
                _g1 = 0
                while (_g1 < len(fields)):
                    field = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                    _g1 = (_g1 + 1)
                    add(field.field)
                    loopI(field.expr)
            elif (loop1 == 6):
                values = _g.params[0]
                add("EArrayDecl")
                Lambda.iter(values,loopI)
            elif (loop1 == 7):
                e1 = _g.params[0]
                params = _g.params[1]
                add("ECall")
                loopI(e1)
                Lambda.iter(params,loopI)
            elif (loop1 == 8):
                tp = _g.params[0]
                params = _g.params[1]
                add(("ENew " + HxOverrides.stringOrNull(_gthis.printTypePath(tp))))
                Lambda.iter(params,loopI)
            elif (loop1 == 9):
                op = _g.params[0]
                postFix = _g.params[1]
                e1 = _g.params[2]
                add(("EUnop " + HxOverrides.stringOrNull(_gthis.printUnop(op))))
                loopI(e1)
            elif (loop1 == 10):
                vars = _g.params[0]
                add("EVars")
                _g1 = 0
                while (_g1 < len(vars)):
                    v = (vars[_g1] if _g1 >= 0 and _g1 < len(vars) else None)
                    _g1 = (_g1 + 1)
                    if (Reflect.field(v,"expr") is not None):
                        add(v.name)
                        loopI(Reflect.field(v,"expr"))
            elif (loop1 == 11):
                _g1 = _g.params[0]
                f = _g.params[1]
                add("EFunction")
                if (Reflect.field(f,"expr") is not None):
                    loopI(Reflect.field(f,"expr"))
            elif (loop1 == 12):
                exprs = _g.params[0]
                add("EBlock")
                Lambda.iter(exprs,loopI)
            elif (loop1 == 13):
                it = _g.params[0]
                expr = _g.params[1]
                add("EFor")
                loopI(it)
                loopI(expr)
            elif (loop1 == 14):
                econd = _g.params[0]
                eif = _g.params[1]
                eelse = _g.params[2]
                add("EIf")
                loopI(econd)
                loopI(eif)
                if (eelse is not None):
                    loopI(eelse)
            elif (loop1 == 15):
                econd = _g.params[0]
                e1 = _g.params[1]
                normalWhile = _g.params[2]
                add("EWhile")
                loopI(econd)
                loopI(e1)
            elif (loop1 == 16):
                e1 = _g.params[0]
                cases = _g.params[1]
                edef = _g.params[2]
                add("ESwitch")
                loopI(e1)
                _g1 = 0
                while (_g1 < len(cases)):
                    c = (cases[_g1] if _g1 >= 0 and _g1 < len(cases) else None)
                    _g1 = (_g1 + 1)
                    _g2 = 0
                    _g3 = c.values
                    while (_g2 < len(_g3)):
                        pat = (_g3[_g2] if _g2 >= 0 and _g2 < len(_g3) else None)
                        _g2 = (_g2 + 1)
                        loop(((("null" if tabs is None else tabs) + HxOverrides.stringOrNull(_gthis.tabString)) + HxOverrides.stringOrNull(_gthis.tabString)),pat)
                    if (Reflect.field(c,"expr") is not None):
                        loop((((("null" if tabs is None else tabs) + HxOverrides.stringOrNull(_gthis.tabString)) + HxOverrides.stringOrNull(_gthis.tabString)) + HxOverrides.stringOrNull(_gthis.tabString)),Reflect.field(c,"expr"))
                if (edef is not None):
                    loop((((("null" if tabs is None else tabs) + HxOverrides.stringOrNull(_gthis.tabString)) + HxOverrides.stringOrNull(_gthis.tabString)) + HxOverrides.stringOrNull(_gthis.tabString)),edef)
            elif (loop1 == 17):
                e1 = _g.params[0]
                catches = _g.params[1]
                add("ETry")
                loopI(e1)
                _g1 = 0
                while (_g1 < len(catches)):
                    c = (catches[_g1] if _g1 >= 0 and _g1 < len(catches) else None)
                    _g1 = (_g1 + 1)
                    loop(((("null" if tabs is None else tabs) + HxOverrides.stringOrNull(_gthis.tabString)) + HxOverrides.stringOrNull(_gthis.tabString)),c.expr)
            elif (loop1 == 18):
                e1 = _g.params[0]
                add("EReturn")
                if (e1 is not None):
                    loopI(e1)
            elif (loop1 == 19):
                add("EBreak")
            elif (loop1 == 20):
                add("EContinue")
            elif (loop1 == 21):
                e1 = _g.params[0]
                add("EUntyped")
                loopI(e1)
            elif (loop1 == 22):
                e1 = _g.params[0]
                add("EThrow")
                loopI(e1)
            elif (loop1 == 23):
                e1 = _g.params[0]
                t = _g.params[1]
                add("ECast")
                loopI(e1)
            elif (loop1 == 24):
                e1 = _g.params[0]
                displayKind = _g.params[1]
                add("EDisplay")
                loopI(e1)
            elif (loop1 == 25):
                t = _g.params[0]
                add("EDisplayNew")
            elif (loop1 == 26):
                econd = _g.params[0]
                eif = _g.params[1]
                eelse = _g.params[2]
                add("ETernary")
                loopI(econd)
                loopI(eif)
                loopI(eelse)
            elif (loop1 == 27):
                e1 = _g.params[0]
                t = _g.params[1]
                add("ECheckType")
                loopI(e1)
            elif (loop1 == 28):
                s = _g.params[0]
                e1 = _g.params[1]
                add(("EMeta " + HxOverrides.stringOrNull(_gthis.printMetadata(s))))
                loopI(e1)
            elif (loop1 == 29):
                e1 = _g.params[0]
                t = _g.params[1]
                add("EIs")
                loopI(e1)
            else:
                pass
        loop = _hx_local_8
        loop("",e)
        return buffer_b.getvalue()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.tabs = None
        _hx_o.tabString = None
haxe_macro_Printer._hx_class = haxe_macro_Printer
_hx_classes["haxe.macro.Printer"] = haxe_macro_Printer

class haxe_macro_Type(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.Type"
    _hx_constructs = ["TMono", "TEnum", "TInst", "TType", "TFun", "TAnonymous", "TDynamic", "TLazy", "TAbstract"]

    @staticmethod
    def TMono(t):
        return haxe_macro_Type("TMono", 0, (t,))

    @staticmethod
    def TEnum(t,params):
        return haxe_macro_Type("TEnum", 1, (t,params))

    @staticmethod
    def TInst(t,params):
        return haxe_macro_Type("TInst", 2, (t,params))

    @staticmethod
    def TType(t,params):
        return haxe_macro_Type("TType", 3, (t,params))

    @staticmethod
    def TFun(args,ret):
        return haxe_macro_Type("TFun", 4, (args,ret))

    @staticmethod
    def TAnonymous(a):
        return haxe_macro_Type("TAnonymous", 5, (a,))

    @staticmethod
    def TDynamic(t):
        return haxe_macro_Type("TDynamic", 6, (t,))

    @staticmethod
    def TLazy(f):
        return haxe_macro_Type("TLazy", 7, (f,))

    @staticmethod
    def TAbstract(t,params):
        return haxe_macro_Type("TAbstract", 8, (t,params))
haxe_macro_Type._hx_class = haxe_macro_Type
_hx_classes["haxe.macro.Type"] = haxe_macro_Type

class haxe_macro_AnonStatus(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.AnonStatus"
    _hx_constructs = ["AClosed", "AOpened", "AConst", "AExtend", "AClassStatics", "AEnumStatics", "AAbstractStatics"]

    @staticmethod
    def AExtend(tl):
        return haxe_macro_AnonStatus("AExtend", 3, (tl,))

    @staticmethod
    def AClassStatics(t):
        return haxe_macro_AnonStatus("AClassStatics", 4, (t,))

    @staticmethod
    def AEnumStatics(t):
        return haxe_macro_AnonStatus("AEnumStatics", 5, (t,))

    @staticmethod
    def AAbstractStatics(t):
        return haxe_macro_AnonStatus("AAbstractStatics", 6, (t,))
haxe_macro_AnonStatus.AClosed = haxe_macro_AnonStatus("AClosed", 0, ())
haxe_macro_AnonStatus.AOpened = haxe_macro_AnonStatus("AOpened", 1, ())
haxe_macro_AnonStatus.AConst = haxe_macro_AnonStatus("AConst", 2, ())
haxe_macro_AnonStatus._hx_class = haxe_macro_AnonStatus
_hx_classes["haxe.macro.AnonStatus"] = haxe_macro_AnonStatus

class haxe_macro_ClassKind(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.ClassKind"
    _hx_constructs = ["KNormal", "KTypeParameter", "KModuleFields", "KExpr", "KGeneric", "KGenericInstance", "KMacroType", "KAbstractImpl", "KGenericBuild"]

    @staticmethod
    def KTypeParameter(constraints):
        return haxe_macro_ClassKind("KTypeParameter", 1, (constraints,))

    @staticmethod
    def KModuleFields(module):
        return haxe_macro_ClassKind("KModuleFields", 2, (module,))

    @staticmethod
    def KExpr(expr):
        return haxe_macro_ClassKind("KExpr", 3, (expr,))

    @staticmethod
    def KGenericInstance(cl,params):
        return haxe_macro_ClassKind("KGenericInstance", 5, (cl,params))

    @staticmethod
    def KAbstractImpl(a):
        return haxe_macro_ClassKind("KAbstractImpl", 7, (a,))
haxe_macro_ClassKind.KNormal = haxe_macro_ClassKind("KNormal", 0, ())
haxe_macro_ClassKind.KGeneric = haxe_macro_ClassKind("KGeneric", 4, ())
haxe_macro_ClassKind.KMacroType = haxe_macro_ClassKind("KMacroType", 6, ())
haxe_macro_ClassKind.KGenericBuild = haxe_macro_ClassKind("KGenericBuild", 8, ())
haxe_macro_ClassKind._hx_class = haxe_macro_ClassKind
_hx_classes["haxe.macro.ClassKind"] = haxe_macro_ClassKind

class haxe_macro_FieldKind(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.FieldKind"
    _hx_constructs = ["FVar", "FMethod"]

    @staticmethod
    def FVar(read,write):
        return haxe_macro_FieldKind("FVar", 0, (read,write))

    @staticmethod
    def FMethod(k):
        return haxe_macro_FieldKind("FMethod", 1, (k,))
haxe_macro_FieldKind._hx_class = haxe_macro_FieldKind
_hx_classes["haxe.macro.FieldKind"] = haxe_macro_FieldKind

class haxe_macro_VarAccess(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.VarAccess"
    _hx_constructs = ["AccNormal", "AccNo", "AccNever", "AccResolve", "AccCall", "AccInline", "AccRequire", "AccCtor"]

    @staticmethod
    def AccRequire(r,msg = None):
        return haxe_macro_VarAccess("AccRequire", 6, (r,msg))
haxe_macro_VarAccess.AccNormal = haxe_macro_VarAccess("AccNormal", 0, ())
haxe_macro_VarAccess.AccNo = haxe_macro_VarAccess("AccNo", 1, ())
haxe_macro_VarAccess.AccNever = haxe_macro_VarAccess("AccNever", 2, ())
haxe_macro_VarAccess.AccResolve = haxe_macro_VarAccess("AccResolve", 3, ())
haxe_macro_VarAccess.AccCall = haxe_macro_VarAccess("AccCall", 4, ())
haxe_macro_VarAccess.AccInline = haxe_macro_VarAccess("AccInline", 5, ())
haxe_macro_VarAccess.AccCtor = haxe_macro_VarAccess("AccCtor", 7, ())
haxe_macro_VarAccess._hx_class = haxe_macro_VarAccess
_hx_classes["haxe.macro.VarAccess"] = haxe_macro_VarAccess

class haxe_macro_MethodKind(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.MethodKind"
    _hx_constructs = ["MethNormal", "MethInline", "MethDynamic", "MethMacro"]
haxe_macro_MethodKind.MethNormal = haxe_macro_MethodKind("MethNormal", 0, ())
haxe_macro_MethodKind.MethInline = haxe_macro_MethodKind("MethInline", 1, ())
haxe_macro_MethodKind.MethDynamic = haxe_macro_MethodKind("MethDynamic", 2, ())
haxe_macro_MethodKind.MethMacro = haxe_macro_MethodKind("MethMacro", 3, ())
haxe_macro_MethodKind._hx_class = haxe_macro_MethodKind
_hx_classes["haxe.macro.MethodKind"] = haxe_macro_MethodKind

class haxe_macro_TConstant(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.TConstant"
    _hx_constructs = ["TInt", "TFloat", "TString", "TBool", "TNull", "TThis", "TSuper"]

    @staticmethod
    def TInt(i):
        return haxe_macro_TConstant("TInt", 0, (i,))

    @staticmethod
    def TFloat(s):
        return haxe_macro_TConstant("TFloat", 1, (s,))

    @staticmethod
    def TString(s):
        return haxe_macro_TConstant("TString", 2, (s,))

    @staticmethod
    def TBool(b):
        return haxe_macro_TConstant("TBool", 3, (b,))
haxe_macro_TConstant.TNull = haxe_macro_TConstant("TNull", 4, ())
haxe_macro_TConstant.TThis = haxe_macro_TConstant("TThis", 5, ())
haxe_macro_TConstant.TSuper = haxe_macro_TConstant("TSuper", 6, ())
haxe_macro_TConstant._hx_class = haxe_macro_TConstant
_hx_classes["haxe.macro.TConstant"] = haxe_macro_TConstant

class haxe_macro_ModuleType(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.ModuleType"
    _hx_constructs = ["TClassDecl", "TEnumDecl", "TTypeDecl", "TAbstract"]

    @staticmethod
    def TClassDecl(c):
        return haxe_macro_ModuleType("TClassDecl", 0, (c,))

    @staticmethod
    def TEnumDecl(e):
        return haxe_macro_ModuleType("TEnumDecl", 1, (e,))

    @staticmethod
    def TTypeDecl(t):
        return haxe_macro_ModuleType("TTypeDecl", 2, (t,))

    @staticmethod
    def TAbstract(a):
        return haxe_macro_ModuleType("TAbstract", 3, (a,))
haxe_macro_ModuleType._hx_class = haxe_macro_ModuleType
_hx_classes["haxe.macro.ModuleType"] = haxe_macro_ModuleType

class haxe_macro_FieldAccess(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.FieldAccess"
    _hx_constructs = ["FInstance", "FStatic", "FAnon", "FDynamic", "FClosure", "FEnum"]

    @staticmethod
    def FInstance(c,params,cf):
        return haxe_macro_FieldAccess("FInstance", 0, (c,params,cf))

    @staticmethod
    def FStatic(c,cf):
        return haxe_macro_FieldAccess("FStatic", 1, (c,cf))

    @staticmethod
    def FAnon(cf):
        return haxe_macro_FieldAccess("FAnon", 2, (cf,))

    @staticmethod
    def FDynamic(s):
        return haxe_macro_FieldAccess("FDynamic", 3, (s,))

    @staticmethod
    def FClosure(c,cf):
        return haxe_macro_FieldAccess("FClosure", 4, (c,cf))

    @staticmethod
    def FEnum(e,ef):
        return haxe_macro_FieldAccess("FEnum", 5, (e,ef))
haxe_macro_FieldAccess._hx_class = haxe_macro_FieldAccess
_hx_classes["haxe.macro.FieldAccess"] = haxe_macro_FieldAccess

class haxe_macro_TypedExprDef(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.TypedExprDef"
    _hx_constructs = ["TConst", "TLocal", "TArray", "TBinop", "TField", "TTypeExpr", "TParenthesis", "TObjectDecl", "TArrayDecl", "TCall", "TNew", "TUnop", "TFunction", "TVar", "TBlock", "TFor", "TIf", "TWhile", "TSwitch", "TTry", "TReturn", "TBreak", "TContinue", "TThrow", "TCast", "TMeta", "TEnumParameter", "TEnumIndex", "TIdent"]

    @staticmethod
    def TConst(c):
        return haxe_macro_TypedExprDef("TConst", 0, (c,))

    @staticmethod
    def TLocal(v):
        return haxe_macro_TypedExprDef("TLocal", 1, (v,))

    @staticmethod
    def TArray(e1,e2):
        return haxe_macro_TypedExprDef("TArray", 2, (e1,e2))

    @staticmethod
    def TBinop(op,e1,e2):
        return haxe_macro_TypedExprDef("TBinop", 3, (op,e1,e2))

    @staticmethod
    def TField(e,fa):
        return haxe_macro_TypedExprDef("TField", 4, (e,fa))

    @staticmethod
    def TTypeExpr(m):
        return haxe_macro_TypedExprDef("TTypeExpr", 5, (m,))

    @staticmethod
    def TParenthesis(e):
        return haxe_macro_TypedExprDef("TParenthesis", 6, (e,))

    @staticmethod
    def TObjectDecl(fields):
        return haxe_macro_TypedExprDef("TObjectDecl", 7, (fields,))

    @staticmethod
    def TArrayDecl(el):
        return haxe_macro_TypedExprDef("TArrayDecl", 8, (el,))

    @staticmethod
    def TCall(e,el):
        return haxe_macro_TypedExprDef("TCall", 9, (e,el))

    @staticmethod
    def TNew(c,params,el):
        return haxe_macro_TypedExprDef("TNew", 10, (c,params,el))

    @staticmethod
    def TUnop(op,postFix,e):
        return haxe_macro_TypedExprDef("TUnop", 11, (op,postFix,e))

    @staticmethod
    def TFunction(tfunc):
        return haxe_macro_TypedExprDef("TFunction", 12, (tfunc,))

    @staticmethod
    def TVar(v,expr):
        return haxe_macro_TypedExprDef("TVar", 13, (v,expr))

    @staticmethod
    def TBlock(el):
        return haxe_macro_TypedExprDef("TBlock", 14, (el,))

    @staticmethod
    def TFor(v,e1,e2):
        return haxe_macro_TypedExprDef("TFor", 15, (v,e1,e2))

    @staticmethod
    def TIf(econd,eif,eelse):
        return haxe_macro_TypedExprDef("TIf", 16, (econd,eif,eelse))

    @staticmethod
    def TWhile(econd,e,normalWhile):
        return haxe_macro_TypedExprDef("TWhile", 17, (econd,e,normalWhile))

    @staticmethod
    def TSwitch(e,cases,edef):
        return haxe_macro_TypedExprDef("TSwitch", 18, (e,cases,edef))

    @staticmethod
    def TTry(e,catches):
        return haxe_macro_TypedExprDef("TTry", 19, (e,catches))

    @staticmethod
    def TReturn(e):
        return haxe_macro_TypedExprDef("TReturn", 20, (e,))

    @staticmethod
    def TThrow(e):
        return haxe_macro_TypedExprDef("TThrow", 23, (e,))

    @staticmethod
    def TCast(e,m):
        return haxe_macro_TypedExprDef("TCast", 24, (e,m))

    @staticmethod
    def TMeta(m,e1):
        return haxe_macro_TypedExprDef("TMeta", 25, (m,e1))

    @staticmethod
    def TEnumParameter(e1,ef,index):
        return haxe_macro_TypedExprDef("TEnumParameter", 26, (e1,ef,index))

    @staticmethod
    def TEnumIndex(e1):
        return haxe_macro_TypedExprDef("TEnumIndex", 27, (e1,))

    @staticmethod
    def TIdent(s):
        return haxe_macro_TypedExprDef("TIdent", 28, (s,))
haxe_macro_TypedExprDef.TBreak = haxe_macro_TypedExprDef("TBreak", 21, ())
haxe_macro_TypedExprDef.TContinue = haxe_macro_TypedExprDef("TContinue", 22, ())
haxe_macro_TypedExprDef._hx_class = haxe_macro_TypedExprDef
_hx_classes["haxe.macro.TypedExprDef"] = haxe_macro_TypedExprDef


class haxe_rtti_Meta:
    _hx_class_name = "haxe.rtti.Meta"
    __slots__ = ()
    _hx_statics = ["getType", "isInterface", "getMeta", "getStatics", "getFields"]

    @staticmethod
    def getType(t):
        meta = haxe_rtti_Meta.getMeta(t)
        if ((meta is None) or ((Reflect.field(meta,"obj") is None))):
            return _hx_AnonObject({})
        else:
            return Reflect.field(meta,"obj")

    @staticmethod
    def isInterface(t):
        raise haxe_Exception.thrown("Something went wrong")

    @staticmethod
    def getMeta(t):
        return Reflect.field(t,"__meta__")

    @staticmethod
    def getStatics(t):
        meta = haxe_rtti_Meta.getMeta(t)
        if ((meta is None) or ((Reflect.field(meta,"statics") is None))):
            return _hx_AnonObject({})
        else:
            return Reflect.field(meta,"statics")

    @staticmethod
    def getFields(t):
        meta = haxe_rtti_Meta.getMeta(t)
        if ((meta is None) or ((Reflect.field(meta,"fields") is None))):
            return _hx_AnonObject({})
        else:
            return Reflect.field(meta,"fields")
haxe_rtti_Meta._hx_class = haxe_rtti_Meta
_hx_classes["haxe.rtti.Meta"] = haxe_rtti_Meta


class haxe_xml__Access_NodeAccess_Impl_:
    _hx_class_name = "haxe.xml._Access.NodeAccess_Impl_"
    __slots__ = ()
    _hx_statics = ["resolve"]

    @staticmethod
    def resolve(this1,name):
        x = this1.elementsNamed(name).next()
        if (x is None):
            xname = None
            if (this1.nodeType == Xml.Document):
                xname = "Document"
            else:
                if (this1.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((this1.nodeType is None)) else _Xml_XmlType_Impl_.toString(this1.nodeType))))))
                xname = this1.nodeName
            raise haxe_Exception.thrown(((("null" if xname is None else xname) + " is missing element ") + ("null" if name is None else name)))
        if ((x.nodeType != Xml.Document) and ((x.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Invalid nodeType " + HxOverrides.stringOrNull((("null" if ((x.nodeType is None)) else _Xml_XmlType_Impl_.toString(x.nodeType))))))
        this1 = x
        return this1
haxe_xml__Access_NodeAccess_Impl_._hx_class = haxe_xml__Access_NodeAccess_Impl_
_hx_classes["haxe.xml._Access.NodeAccess_Impl_"] = haxe_xml__Access_NodeAccess_Impl_


class haxe_xml__Access_AttribAccess_Impl_:
    _hx_class_name = "haxe.xml._Access.AttribAccess_Impl_"
    __slots__ = ()
    _hx_statics = ["resolve", "_hx_set"]

    @staticmethod
    def resolve(this1,name):
        if (this1.nodeType == Xml.Document):
            raise haxe_Exception.thrown(("Cannot access document attribute " + ("null" if name is None else name)))
        v = this1.get(name)
        if (v is None):
            if (this1.nodeType != Xml.Element):
                raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((this1.nodeType is None)) else _Xml_XmlType_Impl_.toString(this1.nodeType))))))
            raise haxe_Exception.thrown(((HxOverrides.stringOrNull(this1.nodeName) + " is missing attribute ") + ("null" if name is None else name)))
        return v

    @staticmethod
    def _hx_set(this1,name,value):
        if (this1.nodeType == Xml.Document):
            raise haxe_Exception.thrown(("Cannot access document attribute " + ("null" if name is None else name)))
        this1.set(name,value)
        return value
haxe_xml__Access_AttribAccess_Impl_._hx_class = haxe_xml__Access_AttribAccess_Impl_
_hx_classes["haxe.xml._Access.AttribAccess_Impl_"] = haxe_xml__Access_AttribAccess_Impl_


class haxe_xml__Access_HasAttribAccess_Impl_:
    _hx_class_name = "haxe.xml._Access.HasAttribAccess_Impl_"
    __slots__ = ()
    _hx_statics = ["resolve"]

    @staticmethod
    def resolve(this1,name):
        if (this1.nodeType == Xml.Document):
            raise haxe_Exception.thrown(("Cannot access document attribute " + ("null" if name is None else name)))
        return this1.exists(name)
haxe_xml__Access_HasAttribAccess_Impl_._hx_class = haxe_xml__Access_HasAttribAccess_Impl_
_hx_classes["haxe.xml._Access.HasAttribAccess_Impl_"] = haxe_xml__Access_HasAttribAccess_Impl_


class haxe_xml__Access_HasNodeAccess_Impl_:
    _hx_class_name = "haxe.xml._Access.HasNodeAccess_Impl_"
    __slots__ = ()
    _hx_statics = ["resolve"]

    @staticmethod
    def resolve(this1,name):
        return this1.elementsNamed(name).hasNext()
haxe_xml__Access_HasNodeAccess_Impl_._hx_class = haxe_xml__Access_HasNodeAccess_Impl_
_hx_classes["haxe.xml._Access.HasNodeAccess_Impl_"] = haxe_xml__Access_HasNodeAccess_Impl_


class haxe_xml__Access_NodeListAccess_Impl_:
    _hx_class_name = "haxe.xml._Access.NodeListAccess_Impl_"
    __slots__ = ()
    _hx_statics = ["resolve"]

    @staticmethod
    def resolve(this1,name):
        l = []
        x = this1.elementsNamed(name)
        while x.hasNext():
            x1 = x.next()
            if ((x1.nodeType != Xml.Document) and ((x1.nodeType != Xml.Element))):
                raise haxe_Exception.thrown(("Invalid nodeType " + HxOverrides.stringOrNull((("null" if ((x1.nodeType is None)) else _Xml_XmlType_Impl_.toString(x1.nodeType))))))
            this1 = x1
            l.append(this1)
        return l
haxe_xml__Access_NodeListAccess_Impl_._hx_class = haxe_xml__Access_NodeListAccess_Impl_
_hx_classes["haxe.xml._Access.NodeListAccess_Impl_"] = haxe_xml__Access_NodeListAccess_Impl_


class haxe_xml__Access_Access_Impl_:
    _hx_class_name = "haxe.xml._Access.Access_Impl_"
    __slots__ = ()
    _hx_statics = ["get_x", "get_name", "get_node", "get_nodes", "get_att", "get_has", "get_hasNode", "get_elements", "_new", "get_innerData", "get_innerHTML"]
    x = None
    name = None
    innerData = None
    innerHTML = None
    node = None
    nodes = None
    att = None
    has = None
    hasNode = None
    elements = None

    @staticmethod
    def get_x(this1):
        return this1

    @staticmethod
    def get_name(this1):
        if (this1.nodeType == Xml.Document):
            return "Document"
        else:
            if (this1.nodeType != Xml.Element):
                raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((this1.nodeType is None)) else _Xml_XmlType_Impl_.toString(this1.nodeType))))))
            return this1.nodeName

    @staticmethod
    def get_node(this1):
        return this1

    @staticmethod
    def get_nodes(this1):
        return this1

    @staticmethod
    def get_att(this1):
        return this1

    @staticmethod
    def get_has(this1):
        return this1

    @staticmethod
    def get_hasNode(this1):
        return this1

    @staticmethod
    def get_elements(this1):
        return this1.elements()

    @staticmethod
    def _new(x):
        if ((x.nodeType != Xml.Document) and ((x.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Invalid nodeType " + HxOverrides.stringOrNull((("null" if ((x.nodeType is None)) else _Xml_XmlType_Impl_.toString(x.nodeType))))))
        this1 = x
        return this1

    @staticmethod
    def get_innerData(this1):
        if ((this1.nodeType != Xml.Document) and ((this1.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((this1.nodeType is None)) else _Xml_XmlType_Impl_.toString(this1.nodeType))))))
        it_current = 0
        it_array = this1.children
        if (it_current >= len(it_array)):
            tmp = None
            if (this1.nodeType == Xml.Document):
                tmp = "Document"
            else:
                if (this1.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((this1.nodeType is None)) else _Xml_XmlType_Impl_.toString(this1.nodeType))))))
                tmp = this1.nodeName
            raise haxe_Exception.thrown((("null" if tmp is None else tmp) + " does not have data"))
        v = it_current
        it_current = (it_current + 1)
        v1 = (it_array[v] if v >= 0 and v < len(it_array) else None)
        if (it_current < len(it_array)):
            n = it_current
            it_current = (it_current + 1)
            n1 = (it_array[n] if n >= 0 and n < len(it_array) else None)
            tmp = None
            if ((v1.nodeType == Xml.PCData) and ((n1.nodeType == Xml.CData))):
                if ((v1.nodeType == Xml.Document) or ((v1.nodeType == Xml.Element))):
                    raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((v1.nodeType is None)) else _Xml_XmlType_Impl_.toString(v1.nodeType))))))
                tmp = (StringTools.trim(v1.nodeValue) == "")
            else:
                tmp = False
            if tmp:
                if (it_current >= len(it_array)):
                    if ((n1.nodeType == Xml.Document) or ((n1.nodeType == Xml.Element))):
                        raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((n1.nodeType is None)) else _Xml_XmlType_Impl_.toString(n1.nodeType))))))
                    return n1.nodeValue
                n2 = it_current
                it_current = (it_current + 1)
                n21 = (it_array[n2] if n2 >= 0 and n2 < len(it_array) else None)
                tmp = None
                if (n21.nodeType == Xml.PCData):
                    if ((n21.nodeType == Xml.Document) or ((n21.nodeType == Xml.Element))):
                        raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((n21.nodeType is None)) else _Xml_XmlType_Impl_.toString(n21.nodeType))))))
                    tmp = (StringTools.trim(n21.nodeValue) == "")
                else:
                    tmp = False
                if (tmp and ((it_current >= len(it_array)))):
                    if ((n1.nodeType == Xml.Document) or ((n1.nodeType == Xml.Element))):
                        raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((n1.nodeType is None)) else _Xml_XmlType_Impl_.toString(n1.nodeType))))))
                    return n1.nodeValue
            tmp = None
            if (this1.nodeType == Xml.Document):
                tmp = "Document"
            else:
                if (this1.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((this1.nodeType is None)) else _Xml_XmlType_Impl_.toString(this1.nodeType))))))
                tmp = this1.nodeName
            raise haxe_Exception.thrown((("null" if tmp is None else tmp) + " does not only have data"))
        if ((v1.nodeType != Xml.PCData) and ((v1.nodeType != Xml.CData))):
            tmp = None
            if (this1.nodeType == Xml.Document):
                tmp = "Document"
            else:
                if (this1.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((this1.nodeType is None)) else _Xml_XmlType_Impl_.toString(this1.nodeType))))))
                tmp = this1.nodeName
            raise haxe_Exception.thrown((("null" if tmp is None else tmp) + " does not have data"))
        if ((v1.nodeType == Xml.Document) or ((v1.nodeType == Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((v1.nodeType is None)) else _Xml_XmlType_Impl_.toString(v1.nodeType))))))
        return v1.nodeValue

    @staticmethod
    def get_innerHTML(this1):
        s_b = python_lib_io_StringIO()
        if ((this1.nodeType != Xml.Document) and ((this1.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((this1.nodeType is None)) else _Xml_XmlType_Impl_.toString(this1.nodeType))))))
        _g_current = 0
        _g_array = this1.children
        while (_g_current < len(_g_array)):
            x = _g_current
            _g_current = (_g_current + 1)
            x1 = (_g_array[x] if x >= 0 and x < len(_g_array) else None)
            s_b.write(Std.string(haxe_xml_Printer.print(x1)))
        return s_b.getvalue()
haxe_xml__Access_Access_Impl_._hx_class = haxe_xml__Access_Access_Impl_
_hx_classes["haxe.xml._Access.Access_Impl_"] = haxe_xml__Access_Access_Impl_


class haxe_xml_XmlParserException:
    _hx_class_name = "haxe.xml.XmlParserException"
    __slots__ = ("message", "lineNumber", "positionAtLine", "position", "xml")
    _hx_fields = ["message", "lineNumber", "positionAtLine", "position", "xml"]
    _hx_methods = ["toString"]

    def __init__(self,message,xml,position):
        self.xml = xml
        self.message = message
        self.position = position
        self.lineNumber = 1
        self.positionAtLine = 0
        _g = 0
        _g1 = position
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            c = (-1 if ((i >= len(xml))) else ord(xml[i]))
            if (c == 10):
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.lineNumber
                _hx_local_0.lineNumber = (_hx_local_1 + 1)
                _hx_local_1
                self.positionAtLine = 0
            elif (c != 13):
                _hx_local_2 = self
                _hx_local_3 = _hx_local_2.positionAtLine
                _hx_local_2.positionAtLine = (_hx_local_3 + 1)
                _hx_local_3

    def toString(self):
        return ((((((HxOverrides.stringOrNull(Type.getClassName(Type.getClass(self))) + ": ") + HxOverrides.stringOrNull(self.message)) + " at line ") + Std.string(self.lineNumber)) + " char ") + Std.string(self.positionAtLine))

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.message = None
        _hx_o.lineNumber = None
        _hx_o.positionAtLine = None
        _hx_o.position = None
        _hx_o.xml = None
haxe_xml_XmlParserException._hx_class = haxe_xml_XmlParserException
_hx_classes["haxe.xml.XmlParserException"] = haxe_xml_XmlParserException


class haxe_xml_Parser:
    _hx_class_name = "haxe.xml.Parser"
    __slots__ = ()
    _hx_statics = ["escapes", "parse", "doParse", "isValidChar"]

    @staticmethod
    def parse(_hx_str,strict = None):
        if (strict is None):
            strict = False
        doc = Xml.createDocument()
        haxe_xml_Parser.doParse(_hx_str,strict,0,doc)
        return doc

    @staticmethod
    def doParse(_hx_str,strict,p = None,parent = None):
        if (p is None):
            p = 0
        xml = None
        state = 1
        next = 1
        aname = None
        start = 0
        nsubs = 0
        nbrackets = 0
        buf = StringBuf()
        escapeNext = 1
        attrValQuote = -1
        while (p < len(_hx_str)):
            c = ord(_hx_str[p])
            state1 = state
            if (state1 == 0):
                c1 = c
                if ((((c1 == 32) or ((c1 == 13))) or ((c1 == 10))) or ((c1 == 9))):
                    pass
                else:
                    state = next
                    continue
            elif (state1 == 1):
                if (c == 60):
                    state = 0
                    next = 2
                else:
                    start = p
                    state = 13
                    continue
            elif (state1 == 2):
                c2 = c
                if (c2 == 33):
                    index = (p + 1)
                    if (((-1 if ((index >= len(_hx_str))) else ord(_hx_str[index]))) == 91):
                        p = (p + 2)
                        if (HxString.substr(_hx_str,p,6).upper() != "CDATA["):
                            raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected <![CDATA[",_hx_str,p))
                        p = (p + 5)
                        state = 17
                        start = (p + 1)
                    else:
                        tmp = None
                        index1 = (p + 1)
                        if (((-1 if ((index1 >= len(_hx_str))) else ord(_hx_str[index1]))) != 68):
                            index2 = (p + 1)
                            tmp = (((-1 if ((index2 >= len(_hx_str))) else ord(_hx_str[index2]))) == 100)
                        else:
                            tmp = True
                        if tmp:
                            if (HxString.substr(_hx_str,(p + 2),6).upper() != "OCTYPE"):
                                raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected <!DOCTYPE",_hx_str,p))
                            p = (p + 8)
                            state = 16
                            start = (p + 1)
                        else:
                            tmp1 = None
                            index3 = (p + 1)
                            if (((-1 if ((index3 >= len(_hx_str))) else ord(_hx_str[index3]))) == 45):
                                index4 = (p + 2)
                                tmp1 = (((-1 if ((index4 >= len(_hx_str))) else ord(_hx_str[index4]))) != 45)
                            else:
                                tmp1 = True
                            if tmp1:
                                raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected <!--",_hx_str,p))
                            else:
                                p = (p + 2)
                                state = 15
                                start = (p + 1)
                elif (c2 == 47):
                    if (parent is None):
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected node name",_hx_str,p))
                    start = (p + 1)
                    state = 0
                    next = 10
                elif (c2 == 63):
                    state = 14
                    start = p
                else:
                    state = 3
                    start = p
                    continue
            elif (state1 == 3):
                if (not (((((((((c >= 97) and ((c <= 122))) or (((c >= 65) and ((c <= 90))))) or (((c >= 48) and ((c <= 57))))) or ((c == 58))) or ((c == 46))) or ((c == 95))) or ((c == 45))))):
                    if (p == start):
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected node name",_hx_str,p))
                    xml = Xml.createElement(HxString.substr(_hx_str,start,(p - start)))
                    parent.addChild(xml)
                    nsubs = (nsubs + 1)
                    state = 0
                    next = 4
                    continue
            elif (state1 == 4):
                c3 = c
                if (c3 == 47):
                    state = 11
                elif (c3 == 62):
                    state = 9
                else:
                    state = 5
                    start = p
                    continue
            elif (state1 == 5):
                if (not (((((((((c >= 97) and ((c <= 122))) or (((c >= 65) and ((c <= 90))))) or (((c >= 48) and ((c <= 57))))) or ((c == 58))) or ((c == 46))) or ((c == 95))) or ((c == 45))))):
                    if (start == p):
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected attribute name",_hx_str,p))
                    tmp2 = HxString.substr(_hx_str,start,(p - start))
                    aname = tmp2
                    if xml.exists(aname):
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException((("Duplicate attribute [" + ("null" if aname is None else aname)) + "]"),_hx_str,p))
                    state = 0
                    next = 6
                    continue
            elif (state1 == 6):
                if (c == 61):
                    state = 0
                    next = 7
                else:
                    raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected =",_hx_str,p))
            elif (state1 == 7):
                c4 = c
                if ((c4 == 39) or ((c4 == 34))):
                    buf = StringBuf()
                    state = 8
                    start = (p + 1)
                    attrValQuote = c
                else:
                    raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected \"",_hx_str,p))
            elif (state1 == 8):
                c5 = c
                if (c5 == 38):
                    _hx_len = (p - start)
                    s = (HxString.substr(_hx_str,start,None) if ((_hx_len is None)) else HxString.substr(_hx_str,start,_hx_len))
                    buf.b.write(s)
                    state = 18
                    escapeNext = 8
                    start = (p + 1)
                elif ((c5 == 62) or ((c5 == 60))):
                    if strict:
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException((("Invalid unescaped " + HxOverrides.stringOrNull("".join(map(chr,[c])))) + " in attribute value"),_hx_str,p))
                    elif (c == attrValQuote):
                        len1 = (p - start)
                        s1 = (HxString.substr(_hx_str,start,None) if ((len1 is None)) else HxString.substr(_hx_str,start,len1))
                        buf.b.write(s1)
                        val = buf.b.getvalue()
                        buf = StringBuf()
                        xml.set(aname,val)
                        state = 0
                        next = 4
                elif (c == attrValQuote):
                    len2 = (p - start)
                    s2 = (HxString.substr(_hx_str,start,None) if ((len2 is None)) else HxString.substr(_hx_str,start,len2))
                    buf.b.write(s2)
                    val1 = buf.b.getvalue()
                    buf = StringBuf()
                    xml.set(aname,val1)
                    state = 0
                    next = 4
            elif (state1 == 9):
                p = haxe_xml_Parser.doParse(_hx_str,strict,p,xml)
                start = p
                state = 1
            elif (state1 == 10):
                if (not (((((((((c >= 97) and ((c <= 122))) or (((c >= 65) and ((c <= 90))))) or (((c >= 48) and ((c <= 57))))) or ((c == 58))) or ((c == 46))) or ((c == 95))) or ((c == 45))))):
                    if (start == p):
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected node name",_hx_str,p))
                    v = HxString.substr(_hx_str,start,(p - start))
                    if ((parent is None) or ((parent.nodeType != 0))):
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException((("Unexpected </" + ("null" if v is None else v)) + ">, tag is not open"),_hx_str,p))
                    if (parent.nodeType != Xml.Element):
                        raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((parent.nodeType is None)) else _Xml_XmlType_Impl_.toString(parent.nodeType))))))
                    if (v != parent.nodeName):
                        if (parent.nodeType != Xml.Element):
                            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((parent.nodeType is None)) else _Xml_XmlType_Impl_.toString(parent.nodeType))))))
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException((("Expected </" + HxOverrides.stringOrNull(parent.nodeName)) + ">"),_hx_str,p))
                    state = 0
                    next = 12
                    continue
            elif (state1 == 11):
                if (c == 62):
                    state = 1
                else:
                    raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected >",_hx_str,p))
            elif (state1 == 12):
                if (c == 62):
                    if (nsubs == 0):
                        parent.addChild(Xml.createPCData(""))
                    return p
                else:
                    raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected >",_hx_str,p))
            elif (state1 == 13):
                if (c == 60):
                    len3 = (p - start)
                    s3 = (HxString.substr(_hx_str,start,None) if ((len3 is None)) else HxString.substr(_hx_str,start,len3))
                    buf.b.write(s3)
                    child = Xml.createPCData(buf.b.getvalue())
                    buf = StringBuf()
                    parent.addChild(child)
                    nsubs = (nsubs + 1)
                    state = 0
                    next = 2
                elif (c == 38):
                    len4 = (p - start)
                    s4 = (HxString.substr(_hx_str,start,None) if ((len4 is None)) else HxString.substr(_hx_str,start,len4))
                    buf.b.write(s4)
                    state = 18
                    escapeNext = 13
                    start = (p + 1)
            elif (state1 == 14):
                tmp3 = None
                if (c == 63):
                    index5 = (p + 1)
                    tmp3 = (((-1 if ((index5 >= len(_hx_str))) else ord(_hx_str[index5]))) == 62)
                else:
                    tmp3 = False
                if tmp3:
                    p = (p + 1)
                    str1 = HxString.substr(_hx_str,(start + 1),((p - start) - 2))
                    parent.addChild(Xml.createProcessingInstruction(str1))
                    nsubs = (nsubs + 1)
                    state = 1
            elif (state1 == 15):
                tmp4 = None
                tmp5 = None
                if (c == 45):
                    index6 = (p + 1)
                    tmp5 = (((-1 if ((index6 >= len(_hx_str))) else ord(_hx_str[index6]))) == 45)
                else:
                    tmp5 = False
                if tmp5:
                    index7 = (p + 2)
                    tmp4 = (((-1 if ((index7 >= len(_hx_str))) else ord(_hx_str[index7]))) == 62)
                else:
                    tmp4 = False
                if tmp4:
                    parent.addChild(Xml.createComment(HxString.substr(_hx_str,start,(p - start))))
                    nsubs = (nsubs + 1)
                    p = (p + 2)
                    state = 1
            elif (state1 == 16):
                if (c == 91):
                    nbrackets = (nbrackets + 1)
                elif (c == 93):
                    nbrackets = (nbrackets - 1)
                elif ((c == 62) and ((nbrackets == 0))):
                    parent.addChild(Xml.createDocType(HxString.substr(_hx_str,start,(p - start))))
                    nsubs = (nsubs + 1)
                    state = 1
            elif (state1 == 17):
                tmp6 = None
                tmp7 = None
                if (c == 93):
                    index8 = (p + 1)
                    tmp7 = (((-1 if ((index8 >= len(_hx_str))) else ord(_hx_str[index8]))) == 93)
                else:
                    tmp7 = False
                if tmp7:
                    index9 = (p + 2)
                    tmp6 = (((-1 if ((index9 >= len(_hx_str))) else ord(_hx_str[index9]))) == 62)
                else:
                    tmp6 = False
                if tmp6:
                    child1 = Xml.createCData(HxString.substr(_hx_str,start,(p - start)))
                    parent.addChild(child1)
                    nsubs = (nsubs + 1)
                    p = (p + 2)
                    state = 1
            elif (state1 == 18):
                if (c == 59):
                    s5 = HxString.substr(_hx_str,start,(p - start))
                    if (((-1 if ((0 >= len(s5))) else ord(s5[0]))) == 35):
                        c6 = (Std.parseInt(("0" + HxOverrides.stringOrNull(HxString.substr(s5,1,(len(s5) - 1))))) if ((((-1 if ((1 >= len(s5))) else ord(s5[1]))) == 120)) else Std.parseInt(HxString.substr(s5,1,(len(s5) - 1))))
                        s6 = "".join(map(chr,[c6]))
                        buf.b.write(s6)
                    elif (not (s5 in haxe_xml_Parser.escapes.h)):
                        if strict:
                            raise haxe_Exception.thrown(haxe_xml_XmlParserException(("Undefined entity: " + ("null" if s5 is None else s5)),_hx_str,p))
                        s7 = Std.string((("&" + ("null" if s5 is None else s5)) + ";"))
                        buf.b.write(s7)
                    else:
                        s8 = Std.string(haxe_xml_Parser.escapes.h.get(s5,None))
                        buf.b.write(s8)
                    start = (p + 1)
                    state = escapeNext
                elif ((not (((((((((c >= 97) and ((c <= 122))) or (((c >= 65) and ((c <= 90))))) or (((c >= 48) and ((c <= 57))))) or ((c == 58))) or ((c == 46))) or ((c == 95))) or ((c == 45))))) and ((c != 35))):
                    if strict:
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException(("Invalid character in entity: " + HxOverrides.stringOrNull("".join(map(chr,[c])))),_hx_str,p))
                    s9 = "".join(map(chr,[38]))
                    buf.b.write(s9)
                    len5 = (p - start)
                    s10 = (HxString.substr(_hx_str,start,None) if ((len5 is None)) else HxString.substr(_hx_str,start,len5))
                    buf.b.write(s10)
                    p = (p - 1)
                    start = (p + 1)
                    state = escapeNext
            else:
                pass
            p = (p + 1)
        if (state == 1):
            start = p
            state = 13
        if (state == 13):
            if (parent.nodeType == 0):
                if (parent.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((parent.nodeType is None)) else _Xml_XmlType_Impl_.toString(parent.nodeType))))))
                raise haxe_Exception.thrown(haxe_xml_XmlParserException((("Unclosed node <" + HxOverrides.stringOrNull(parent.nodeName)) + ">"),_hx_str,p))
            if ((p != start) or ((nsubs == 0))):
                _hx_len = (p - start)
                s = (HxString.substr(_hx_str,start,None) if ((_hx_len is None)) else HxString.substr(_hx_str,start,_hx_len))
                buf.b.write(s)
                parent.addChild(Xml.createPCData(buf.b.getvalue()))
                nsubs = (nsubs + 1)
            return p
        if (((not strict) and ((state == 18))) and ((escapeNext == 13))):
            s = "".join(map(chr,[38]))
            buf.b.write(s)
            _hx_len = (p - start)
            s = (HxString.substr(_hx_str,start,None) if ((_hx_len is None)) else HxString.substr(_hx_str,start,_hx_len))
            buf.b.write(s)
            parent.addChild(Xml.createPCData(buf.b.getvalue()))
            nsubs = (nsubs + 1)
            return p
        raise haxe_Exception.thrown(haxe_xml_XmlParserException("Unexpected end",_hx_str,p))

    @staticmethod
    def isValidChar(c):
        if (not ((((((((c >= 97) and ((c <= 122))) or (((c >= 65) and ((c <= 90))))) or (((c >= 48) and ((c <= 57))))) or ((c == 58))) or ((c == 46))) or ((c == 95))))):
            return (c == 45)
        else:
            return True
haxe_xml_Parser._hx_class = haxe_xml_Parser
_hx_classes["haxe.xml.Parser"] = haxe_xml_Parser


class haxe_xml_Printer:
    _hx_class_name = "haxe.xml.Printer"
    __slots__ = ("output", "pretty")
    _hx_fields = ["output", "pretty"]
    _hx_methods = ["writeNode", "write", "newline", "hasChildren"]
    _hx_statics = ["print"]

    def __init__(self,pretty):
        self.output = StringBuf()
        self.pretty = pretty

    def writeNode(self,value,tabs):
        _g = value.nodeType
        if (_g == 0):
            _this = self.output
            s = Std.string((("null" if tabs is None else tabs) + "<"))
            _this.b.write(s)
            if (value.nodeType != Xml.Element):
                raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
            _this = self.output
            s = Std.string(value.nodeName)
            _this.b.write(s)
            attribute = value.attributes()
            while attribute.hasNext():
                attribute1 = attribute.next()
                _this = self.output
                s = Std.string(((" " + ("null" if attribute1 is None else attribute1)) + "=\""))
                _this.b.write(s)
                input = StringTools.htmlEscape(value.get(attribute1),True)
                _this1 = self.output
                s1 = Std.string(input)
                _this1.b.write(s1)
                self.output.b.write("\"")
            if self.hasChildren(value):
                self.output.b.write(">")
                if self.pretty:
                    self.output.b.write("\n")
                if ((value.nodeType != Xml.Document) and ((value.nodeType != Xml.Element))):
                    raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
                _g_current = 0
                _g_array = value.children
                while (_g_current < len(_g_array)):
                    child = _g_current
                    _g_current = (_g_current + 1)
                    child1 = (_g_array[child] if child >= 0 and child < len(_g_array) else None)
                    self.writeNode(child1,((("null" if tabs is None else tabs) + "\t") if (self.pretty) else tabs))
                _this = self.output
                s = Std.string((("null" if tabs is None else tabs) + "</"))
                _this.b.write(s)
                if (value.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
                _this = self.output
                s = Std.string(value.nodeName)
                _this.b.write(s)
                self.output.b.write(">")
                if self.pretty:
                    self.output.b.write("\n")
            else:
                self.output.b.write("/>")
                if self.pretty:
                    self.output.b.write("\n")
        elif (_g == 1):
            if ((value.nodeType == Xml.Document) or ((value.nodeType == Xml.Element))):
                raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
            nodeValue = value.nodeValue
            if (len(nodeValue) != 0):
                input = (("null" if tabs is None else tabs) + HxOverrides.stringOrNull(StringTools.htmlEscape(nodeValue)))
                _this = self.output
                s = Std.string(input)
                _this.b.write(s)
                if self.pretty:
                    self.output.b.write("\n")
        elif (_g == 2):
            _this = self.output
            s = Std.string((("null" if tabs is None else tabs) + "<![CDATA["))
            _this.b.write(s)
            if ((value.nodeType == Xml.Document) or ((value.nodeType == Xml.Element))):
                raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
            _this = self.output
            s = Std.string(value.nodeValue)
            _this.b.write(s)
            self.output.b.write("]]>")
            if self.pretty:
                self.output.b.write("\n")
        elif (_g == 3):
            if ((value.nodeType == Xml.Document) or ((value.nodeType == Xml.Element))):
                raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
            commentContent = value.nodeValue
            commentContent = EReg("[\n\r\t]+","g").replace(commentContent,"")
            commentContent = (("<!--" + ("null" if commentContent is None else commentContent)) + "-->")
            _this = self.output
            s = Std.string(tabs)
            _this.b.write(s)
            input = StringTools.trim(commentContent)
            _this = self.output
            s = Std.string(input)
            _this.b.write(s)
            if self.pretty:
                self.output.b.write("\n")
        elif (_g == 4):
            if ((value.nodeType == Xml.Document) or ((value.nodeType == Xml.Element))):
                raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
            _this = self.output
            s = Std.string((("<!DOCTYPE " + HxOverrides.stringOrNull(value.nodeValue)) + ">"))
            _this.b.write(s)
            if self.pretty:
                self.output.b.write("\n")
        elif (_g == 5):
            if ((value.nodeType == Xml.Document) or ((value.nodeType == Xml.Element))):
                raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
            _this = self.output
            s = Std.string((("<?" + HxOverrides.stringOrNull(value.nodeValue)) + "?>"))
            _this.b.write(s)
            if self.pretty:
                self.output.b.write("\n")
        elif (_g == 6):
            if ((value.nodeType != Xml.Document) and ((value.nodeType != Xml.Element))):
                raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
            _g_current = 0
            _g_array = value.children
            while (_g_current < len(_g_array)):
                child = _g_current
                _g_current = (_g_current + 1)
                child1 = (_g_array[child] if child >= 0 and child < len(_g_array) else None)
                self.writeNode(child1,tabs)
        else:
            pass

    def write(self,input):
        _this = self.output
        s = Std.string(input)
        _this.b.write(s)

    def newline(self):
        if self.pretty:
            self.output.b.write("\n")

    def hasChildren(self,value):
        if ((value.nodeType != Xml.Document) and ((value.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
        _g_current = 0
        _g_array = value.children
        while (_g_current < len(_g_array)):
            child = _g_current
            _g_current = (_g_current + 1)
            child1 = (_g_array[child] if child >= 0 and child < len(_g_array) else None)
            _g = child1.nodeType
            if ((_g == 1) or ((_g == 0))):
                return True
            elif ((_g == 3) or ((_g == 2))):
                if ((child1.nodeType == Xml.Document) or ((child1.nodeType == Xml.Element))):
                    raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((child1.nodeType is None)) else _Xml_XmlType_Impl_.toString(child1.nodeType))))))
                if (len(StringTools.ltrim(child1.nodeValue)) != 0):
                    return True
            else:
                pass
        return False

    @staticmethod
    def print(xml,pretty = None):
        if (pretty is None):
            pretty = False
        printer = haxe_xml_Printer(pretty)
        printer.writeNode(xml,"")
        return printer.output.b.getvalue()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.output = None
        _hx_o.pretty = None
haxe_xml_Printer._hx_class = haxe_xml_Printer
_hx_classes["haxe.xml.Printer"] = haxe_xml_Printer


class pyextern_Main:
    _hx_class_name = "pyextern.Main"
    __slots__ = ("tds", "modules", "processors", "defaultProcessor", "filterModules")
    _hx_fields = ["tds", "modules", "processors", "defaultProcessor", "filterModules"]
    _hx_methods = ["write", "getProcessor", "processModule", "getTd"]
    _hx_statics = ["hxName", "re_ident", "re_type", "isHxKeyword", "main"]

    def __init__(self):
        self.filterModules = None
        self.defaultProcessor = pyextern_Processor()
        _g = haxe_ds_StringMap()
        _g1_head = CompileTimeClassList.get("null,true,pyextern.Processor").h
        while (_g1_head is not None):
            val = _g1_head.item
            _g1_head = _g1_head.next
            cls = val
            _g1 = 0
            _g2 = Reflect.field(haxe_rtti_Meta.getType(cls),"process_modules")
            while (_g1 < len(_g2)):
                m = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
                _g1 = (_g1 + 1)
                value = cls(*[])
                _g.h[m] = value
        self.processors = _g
        self.modules = haxe_ds_StringMap()
        self.tds = haxe_ds_StringMap()

    def write(self,outPath):
        _gthis = self
        def _hx_local_2(m):
            real_td = _gthis.getTd(m,"",False)
            if (real_td is None):
                def _hx_local_0(_):
                    return True
                return _hx_local_0
            _this = real_td.pack
            pack = ".".join([python_Boot.toString1(x1,'') for x1 in _this]).lower()
            hxName = HxString.substr(real_td.name,0,-len("_Module")).lower()
            def _hx_local_1(td):
                if (td.name.lower() == hxName):
                    _this = td.pack
                    return (".".join([python_Boot.toString1(x1,'') for x1 in _this]).lower() == pack)
                else:
                    return False
            return _hx_local_1
        collide = _hx_local_2
        _g = []
        m = self.modules.keys()
        while m.hasNext():
            m1 = m.next()
            if (not Lambda.exists(self.tds,collide(m1))):
                _g.append(m1)
        canTypedef = _g
        _g = 0
        while (_g < len(canTypedef)):
            m = (canTypedef[_g] if _g >= 0 and _g < len(canTypedef) else None)
            _g = (_g + 1)
            real_td = self.getTd(m,"")
            try:
                td = self.getTd(m,HxString.substr(real_td.name,0,-len("_Module")))
                Reflect.setField(td,"meta",[])
                Reflect.setField(td,"isExtern",False)
                td.kind = haxe_macro_TypeDefKind.TDAlias(haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': real_td.pack, 'name': real_td.name})))
            except BaseException as _g1:
                None
        sys_FileSystem.createDirectory(outPath)
        Sys.setCwd(outPath)
        printer = haxe_macro_Printer()
        td = self.tds.iterator()
        while td.hasNext():
            td1 = td.next()
            clsStr = ("/* This file is generated, do not edit! */\n" + HxOverrides.stringOrNull(printer.printTypeDefinition(td1)))
            packDir = haxe_io_Path.join(td1.pack)
            if (packDir != ""):
                sys_FileSystem.createDirectory(packDir)
            path = haxe_io_Path.join([packDir, (HxOverrides.stringOrNull(td1.name) + ".hx")])
            sys_io_File.saveContent(path,clsStr)

    def getProcessor(self,moduleName):
        m = moduleName
        while True:
            if (m in self.processors.h):
                return self.processors.h.get(m,None)
            startIndex = None
            _hx_len = None
            if (startIndex is None):
                _hx_len = m.rfind(".", 0, len(m))
            else:
                i = m.rfind(".", 0, (startIndex + 1))
                startLeft = (max(0,((startIndex + 1) - len("."))) if ((i == -1)) else (i + 1))
                check = m.find(".", startLeft, len(m))
                _hx_len = (check if (((check > i) and ((check <= startIndex)))) else i)
            m = HxString.substr(m,0,_hx_len)
            if (not ((m != ""))):
                break
        return self.defaultProcessor

    def processModule(self,module,moduleName):
        if ((moduleName is not None) and (not self.filterModules(moduleName))):
            return
        if Std.isOfType(module,str):
            moduleName = module
            try:
                _hx_str = Std.string(("trying to import module: " + ("null" if moduleName is None else moduleName)))
                python_Lib.printString((("" + ("null" if _hx_str is None else _hx_str)) + HxOverrides.stringOrNull(python_Lib.lineEnd)))
                module = importlib_Importlib_Module.import_module(moduleName)
            except BaseException as _g:
                None
                haxe_Log.trace(("cannot import " + ("null" if moduleName is None else moduleName)),_hx_AnonObject({'fileName': "src/pyextern/Main.hx", 'lineNumber': 96, 'className': "pyextern.Main", 'methodName': "processModule"}))
                return
        if (not inspect_Inspect_Module.ismodule(module)):
            _hx_str = Std.string(("not module: " + Std.string(module)))
            python_Lib.printString((("" + ("null" if _hx_str is None else _hx_str)) + HxOverrides.stringOrNull(python_Lib.lineEnd)))
            return
        if (moduleName is None):
            moduleName = Reflect.field(Reflect.field(module,"__spec__"),"name")
        if ((moduleName in self.modules.h) or (not self.filterModules(moduleName))):
            return
        _hx_str = Std.string(("process module: " + ("null" if moduleName is None else moduleName)))
        python_Lib.printString((("" + ("null" if _hx_str is None else _hx_str)) + HxOverrides.stringOrNull(python_Lib.lineEnd)))
        v = module
        self.modules.h[moduleName] = v
        proc = self.getProcessor(moduleName)
        proc.processModule(module,moduleName,self)

    def getTd(self,module,fullname,create = None):
        if (create is None):
            create = True
        _g = []
        _g1 = 0
        _g2 = module.split(".")
        while (_g1 < len(_g2)):
            p = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
            _g1 = (_g1 + 1)
            p = pyextern_Utils.lowerCaseFirstLetter(p)
            if pyextern_Main.isHxKeyword(p):
                p = ("_" + ("null" if p is None else p))
            _g.append(p)
        pack = _g
        hxName = None
        if (fullname == ""):
            _g = len(pack)
            if (_g == 0):
                raise haxe_Exception.thrown("top-level?")
            elif (_g == 1):
                hxName = pyextern_Main.hxName((HxOverrides.stringOrNull((pack[0] if 0 < len(pack) else None)) + "_Module"))
            else:
                hxName = pyextern_Main.hxName((HxOverrides.stringOrNull(python_internal_ArrayImpl._get(pack, (len(pack) - 1))) + "_Module"))
        else:
            hxName = pyextern_Main.hxName(fullname)
        _this = (pack + [hxName])
        hxFullName = ".".join([python_Boot.toString1(x1,'') for x1 in _this])
        pythonImportParams = ([_hx_AnonObject({'expr': haxe_macro_ExprDef.EConst(haxe_macro_Constant.CString(module)), 'pos': None})] if ((fullname == "")) else [_hx_AnonObject({'expr': haxe_macro_ExprDef.EConst(haxe_macro_Constant.CString(module)), 'pos': None}), _hx_AnonObject({'expr': haxe_macro_ExprDef.EConst(haxe_macro_Constant.CString(fullname)), 'pos': None})])
        _g = self.tds.h.get(hxFullName,None)
        if (_g is None):
            if (not create):
                return None
            elif create:
                def _hx_local_1(td):
                    if (td.name.lower() == hxName.lower()):
                        _this = td.pack
                        return (".".join([python_Boot.toString1(x1,'') for x1 in _this]).lower() == ".".join([python_Boot.toString1(x1,'') for x1 in pack]).lower())
                    else:
                        return False
                td = Lambda.find(self.tds,_hx_local_1)
                if (td is not None):
                    _this = (td.pack + [td.name])
                    hxFullName_conflict = ".".join([python_Boot.toString1(x1,'') for x1 in _this])
                    _g1 = td.kind
                    tmp = None
                    if (_g1.index == 3):
                        _g2 = _g1.params[0]
                        tmp = True
                    else:
                        tmp = False
                    if tmp:
                        self.tds.remove(hxFullName_conflict)
                    else:
                        raise haxe_Exception.thrown((((("Cannot create " + ("null" if hxFullName is None else hxFullName)) + " because there is already ") + ("null" if hxFullName_conflict is None else hxFullName_conflict)) + " "))
                v = _hx_AnonObject({'pack': pack, 'name': hxName, 'pos': None, 'meta': [_hx_AnonObject({'name': ":pythonImport", 'params': pythonImportParams, 'pos': None})], 'params': [], 'isExtern': True, 'kind': haxe_macro_TypeDefKind.TDClass(), 'fields': []})
                self.tds.h[hxFullName] = v
                return v
            else:
                td = _g
                if Reflect.field(td,"isExtern"):
                    _g1 = python_internal_ArrayImpl._get(Reflect.field(td,"meta"), 0)
                    _g2 = Reflect.field(_g1,"params")
                    _g3 = _g1.pos
                    if (_g1.name == ":pythonImport"):
                        if (_g2 is None):
                            nativeMeta = _g1
                            raise haxe_Exception.thrown(nativeMeta)
                        else:
                            _g3 = len(_g2)
                            if (_g3 == 1):
                                _g3 = (_g2[0] if 0 < len(_g2) else None)
                                _g4 = _g3.expr
                                _g5 = _g3.pos
                                if (_g4.index == 0):
                                    _g3 = _g4.params[0]
                                    if (_g3.index == 2):
                                        _g4 = _g3.params[1]
                                        module = _g3.params[0]
                                        if (fullname != ""):
                                            nativeMeta = _g1
                                            raise haxe_Exception.thrown(nativeMeta)
                                    else:
                                        nativeMeta = _g1
                                        raise haxe_Exception.thrown(nativeMeta)
                                else:
                                    nativeMeta = _g1
                                    raise haxe_Exception.thrown(nativeMeta)
                            elif (_g3 == 2):
                                _g3 = (_g2[0] if 0 < len(_g2) else None)
                                _g4 = (_g2[1] if 1 < len(_g2) else None)
                                _g2 = _g3.expr
                                _g5 = _g3.pos
                                if (_g2.index == 0):
                                    _g3 = _g2.params[0]
                                    if (_g3.index == 2):
                                        _g2 = _g3.params[1]
                                        _g2 = _g4.expr
                                        _g5 = _g4.pos
                                        if (_g2.index == 0):
                                            _g4 = _g2.params[0]
                                            if (_g4.index == 2):
                                                _g2 = _g4.params[1]
                                                fullname1 = _g4.params[0]
                                                module = _g3.params[0]
                                            else:
                                                nativeMeta = _g1
                                                raise haxe_Exception.thrown(nativeMeta)
                                        else:
                                            nativeMeta = _g1
                                            raise haxe_Exception.thrown(nativeMeta)
                                    else:
                                        nativeMeta = _g1
                                        raise haxe_Exception.thrown(nativeMeta)
                                else:
                                    nativeMeta = _g1
                                    raise haxe_Exception.thrown(nativeMeta)
                            else:
                                nativeMeta = _g1
                                raise haxe_Exception.thrown(nativeMeta)
                    else:
                        nativeMeta = _g1
                        raise haxe_Exception.thrown(nativeMeta)
                return td
        else:
            td = _g
            if Reflect.field(td,"isExtern"):
                _g = python_internal_ArrayImpl._get(Reflect.field(td,"meta"), 0)
                _g1 = Reflect.field(_g,"params")
                _g2 = _g.pos
                if (_g.name == ":pythonImport"):
                    if (_g1 is None):
                        nativeMeta = _g
                        raise haxe_Exception.thrown(nativeMeta)
                    else:
                        _g2 = len(_g1)
                        if (_g2 == 1):
                            _g2 = (_g1[0] if 0 < len(_g1) else None)
                            _g3 = _g2.expr
                            _g4 = _g2.pos
                            if (_g3.index == 0):
                                _g2 = _g3.params[0]
                                if (_g2.index == 2):
                                    _g3 = _g2.params[1]
                                    module = _g2.params[0]
                                    if (fullname != ""):
                                        nativeMeta = _g
                                        raise haxe_Exception.thrown(nativeMeta)
                                else:
                                    nativeMeta = _g
                                    raise haxe_Exception.thrown(nativeMeta)
                            else:
                                nativeMeta = _g
                                raise haxe_Exception.thrown(nativeMeta)
                        elif (_g2 == 2):
                            _g2 = (_g1[0] if 0 < len(_g1) else None)
                            _g3 = (_g1[1] if 1 < len(_g1) else None)
                            _g1 = _g2.expr
                            _g4 = _g2.pos
                            if (_g1.index == 0):
                                _g2 = _g1.params[0]
                                if (_g2.index == 2):
                                    _g1 = _g2.params[1]
                                    _g1 = _g3.expr
                                    _g4 = _g3.pos
                                    if (_g1.index == 0):
                                        _g3 = _g1.params[0]
                                        if (_g3.index == 2):
                                            _g1 = _g3.params[1]
                                            fullname = _g3.params[0]
                                            module = _g2.params[0]
                                        else:
                                            nativeMeta = _g
                                            raise haxe_Exception.thrown(nativeMeta)
                                    else:
                                        nativeMeta = _g
                                        raise haxe_Exception.thrown(nativeMeta)
                                else:
                                    nativeMeta = _g
                                    raise haxe_Exception.thrown(nativeMeta)
                            else:
                                nativeMeta = _g
                                raise haxe_Exception.thrown(nativeMeta)
                        else:
                            nativeMeta = _g
                            raise haxe_Exception.thrown(nativeMeta)
                else:
                    nativeMeta = _g
                    raise haxe_Exception.thrown(nativeMeta)
            return td

    @staticmethod
    def hxName(name):
        if (name == ""):
            return ""
        name = pyextern_Utils.upperCaseFirstLetter(name)
        name = StringTools.replace(name,".","_")
        _this = pyextern_Main.re_type
        _this.matchObj = python_lib_Re.search(_this.pattern,name)
        if (_this.matchObj is None):
            raise haxe_Exception.thrown(("invalid class name: " + ("null" if name is None else name)))
        return name

    @staticmethod
    def isHxKeyword(name):
        return (python_internal_ArrayImpl.indexOf(["function", "class", "static", "var", "if", "else", "while", "do", "for", "break", "return", "continue", "extends", "implements", "import", "switch", "case", "default", "public", "private", "try", "untyped", "catch", "new", "this", "throw", "extern", "enum", "in", "interface", "cast", "override", "dynamic", "typedef", "package", "inline", "using", "null", "true", "false", "abstract", "macro", "__init__", "overload", "operator", "final", "is"],name,None) >= 0)

    @staticmethod
    def main():
        _g = Sys.args()
        if (len(_g) == 2):
            moduleNames = (_g[0] if 0 < len(_g) else None)
            outPath = (_g[1] if 1 < len(_g) else None)
            main = pyextern_Main()
            wantedModuleNames = list(map(StringTools.trim,moduleNames.split(",")))
            def _hx_local_5(modname):
                tmp = None
                def _hx_local_0(wanted):
                    if (modname != wanted):
                        return modname.startswith((("null" if wanted is None else wanted) + "."))
                    else:
                        return True
                def _hx_local_1(mod):
                    return modname.startswith(mod)
                def _hx_local_2(p):
                    return p.startswith("_")
                if (((modname is not None) and Lambda.exists(wantedModuleNames,_hx_local_0)) and ((Lambda.exists(["pandas"],_hx_local_1) or (not Lambda.exists(modname.split("."),_hx_local_2))))):
                    _this = modname.lower()
                    startIndex = None
                    tmp = (((_this.find("test") if ((startIndex is None)) else HxString.indexOfImpl(_this,"test",startIndex))) == -1)
                else:
                    tmp = False
                if tmp:
                    def _hx_local_4():
                        def _hx_local_3(skip):
                            if (modname != skip):
                                return modname.startswith((("null" if skip is None else skip) + "."))
                            else:
                                return True
                        return (not Lambda.exists(["numpy.distutils", "numpy.f2py.__main__", "tensorflow.tools.pip_package", "PyQt5.uic.pyuic"],_hx_local_3))
                    return _hx_local_4()
                else:
                    return False
            main.filterModules = _hx_local_5
            _g = 0
            def _hx_local_6(x):
                return None
            _g1 = python_lib_Builtins.list(pkgutil_Pkgutil_Module.walk_packages(None,"",_hx_local_6))
            while (_g < len(_g1)):
                pkg = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                modname = pkg[1]
                if main.filterModules(modname):
                    main.processModule(modname,modname)
            main.write(sys_FileSystem.absolutePath(outPath))
        else:
            raise haxe_Exception.thrown("There should be exactly 2 arguments: moduleName, outPath")

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.tds = None
        _hx_o.modules = None
        _hx_o.processors = None
        _hx_o.defaultProcessor = None
        _hx_o.filterModules = None
pyextern_Main._hx_class = pyextern_Main
_hx_classes["pyextern.Main"] = pyextern_Main


class pyextern_Processor:
    _hx_class_name = "pyextern.Processor"
    __slots__ = ("currentModule",)
    _hx_fields = ["currentModule"]
    _hx_methods = ["type", "getdoc", "parseRst", "docReturns", "docToFun", "sigToFun", "isFieldStatic", "isMethodStatic", "isMethod", "processModule", "hxType", "hxVal"]
    _hx_statics = ["rstParser", "docDefaults"]

    def __init__(self):
        self.currentModule = None

    def type(self,object):
        return python_lib_Builtins.type(object)

    def getdoc(self,obj):
        doc = inspect_Inspect_Module.getdoc(obj)
        if (doc is None):
            return None
        elif not HxOverrides.eq(doc,inspect_Inspect_Module.getdoc(self.type(obj))):
            return doc.replace("*/","* /")
        else:
            return None

    def parseRst(self,doc):
        document = docutils_utils_Utils_Module.new_document("",pyextern_Processor.docDefaults())
        try:
            pyextern_Processor.rstParser.parse(doc,document)
            return Xml.parse(document.asdom().toxml())
        except BaseException as _g:
            None
            return None

    def docReturns(self,doc):
        xml = self.parseRst(doc)
        if (xml is not None):
            if ((xml.nodeType != Xml.Document) and ((xml.nodeType != Xml.Element))):
                raise haxe_Exception.thrown(("Invalid nodeType " + HxOverrides.stringOrNull((("null" if ((xml.nodeType is None)) else _Xml_XmlType_Impl_.toString(xml.nodeType))))))
            this1 = xml
            def _hx_local_0(sec):
                if haxe_xml__Access_HasNodeAccess_Impl_.resolve(sec,"title"):
                    return (haxe_xml__Access_Access_Impl_.get_innerHTML(haxe_xml__Access_NodeAccess_Impl_.resolve(sec,"title")).lower() == "returns")
                else:
                    return False
            sec = Lambda.find(haxe_xml__Access_NodeListAccess_Impl_.resolve(haxe_xml__Access_NodeAccess_Impl_.resolve(this1,"document"),"section"),_hx_local_0)
            if (sec is not None):
                if (haxe_xml__Access_HasNodeAccess_Impl_.resolve(sec,"definition_list") and haxe_xml__Access_HasNodeAccess_Impl_.resolve(haxe_xml__Access_NodeAccess_Impl_.resolve(haxe_xml__Access_NodeAccess_Impl_.resolve(sec,"definition_list"),"definition_list_item"),"classifier")):
                    retDoc = haxe_xml__Access_Access_Impl_.get_innerHTML(haxe_xml__Access_NodeAccess_Impl_.resolve(haxe_xml__Access_NodeAccess_Impl_.resolve(haxe_xml__Access_NodeAccess_Impl_.resolve(sec,"definition_list"),"definition_list_item"),"classifier"))
                    return self.hxType(retDoc)
                if ((sec is not None) and haxe_xml__Access_HasNodeAccess_Impl_.resolve(sec,"paragraph")):
                    retDoc = haxe_xml__Access_Access_Impl_.get_innerHTML(haxe_xml__Access_NodeAccess_Impl_.resolve(sec,"paragraph"))
                    re = EReg("^([_a-z][A-Za-z0-9]*) ?: ? ([A-Za-z0-9]+)$","")
                    re.matchObj = python_lib_Re.search(re.pattern,retDoc)
                    if (re.matchObj is not None):
                        return self.hxType(re.matchObj.group(2))
        return None

    def docToFun(self,doc):
        _g = self.docReturns(doc)
        tmp = None
        if (_g is None):
            tmp = haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Dynamic", 'params': []}))
        else:
            ret = _g
            tmp = ret
        return _hx_AnonObject({'params': [], 'args': None, 'ret': tmp, 'expr': None})

    def sigToFun(self,sig,doc):
        if (sig is None):
            return None
        docFunc = (self.docToFun(doc) if ((doc is not None)) else None)
        _g = []
        p = python_HaxeIterator(iter(Reflect.field(sig,"parameters").values()))
        while p.hasNext():
            p1 = p.next()
            isVarArgs = (p1.kind is inspect_Parameter.VAR_POSITIONAL)
            isKwargs = (p1.kind is inspect_Parameter.VAR_KEYWORD)
            arg = _hx_AnonObject({'opt': ((isVarArgs or isKwargs) or (not (Reflect.field(p1,"default") is inspect_Parameter.empty))), 'name': (("_" + HxOverrides.stringOrNull(p1.name)) if (pyextern_Main.isHxKeyword(p1.name)) else p1.name), 'type': (haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': ["python"], 'name': "VarArgs", 'params': [haxe_macro_TypeParam.TPType(haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Dynamic", 'params': []})))]})) if isVarArgs else (haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': ["python"], 'name': "KwArgs", 'params': [haxe_macro_TypeParam.TPType(haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Dynamic", 'params': []})))]})) if isKwargs else haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Dynamic", 'params': []}))))})
            _g.append(arg)
        args = _g
        return _hx_AnonObject({'params': [], 'args': args, 'ret': (Reflect.field(docFunc,"ret") if (((docFunc is not None) and ((Reflect.field(docFunc,"ret") is not None)))) else haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Dynamic", 'params': []}))), 'expr': None})

    def isFieldStatic(self,memObj):
        if (not inspect_Inspect_Module.isdatadescriptor(memObj)):
            return (not inspect_Inspect_Module.isgetsetdescriptor(memObj))
        else:
            return False

    def isMethodStatic(self,typeName,clsMemName,clsMemObj,fun):
        staticMethods = ["__new__"]
        instanceMethods = ["__init__"]
        if (python_internal_ArrayImpl.indexOf(staticMethods,clsMemName,None) >= 0):
            return True
        if (python_internal_ArrayImpl.indexOf(instanceMethods,clsMemName,None) >= 0):
            return False
        if (typeName == "staticmethod"):
            return True
        if (fun is not None):
            if (len(fun.args) < 1):
                return True
            return ((fun.args[0] if 0 < len(fun.args) else None).name != "self")
        if inspect_Inspect_Module.ismethoddescriptor(clsMemObj):
            return False
        return False

    def isMethod(self,clsMemObj):
        return python_lib_Builtins.callable(clsMemObj)

    def processModule(self,module,moduleName,main):
        self.currentModule = moduleName
        members = None
        try:
            members = inspect_Inspect_Module.getmembers(module)
        except BaseException as _g:
            None
            haxe_Log.trace(("cannot getmembers of " + ("null" if moduleName is None else moduleName)),_hx_AnonObject({'fileName': "src/pyextern/Processor.hx", 'lineNumber': 173, 'className': "pyextern.Processor", 'methodName': "processModule"}))
            return
        _g = 0
        while (_g < len(members)):
            mem = (members[_g] if _g >= 0 and _g < len(members) else None)
            _g = (_g + 1)
            memName = mem[0]
            memObj = mem[1]
            if inspect_Inspect_Module.ismodule(memObj):
                def _hx_local_2():
                    def _hx_local_1(m):
                        return m.startswith((("null" if moduleName is None else moduleName) + "."))
                    return _hx_local_1
                isSubmodule = _hx_local_2()
                mName = memObj.__name__
                if ((not isSubmodule(mName)) and ((memObj.__spec__ is not None))):
                    mName = memObj.__spec__.name
                if (not isSubmodule(mName)):
                    mName = None
                main.processModule(memObj,mName)
            elif inspect_Inspect_Module.isclass(memObj):
                if ((memObj.__module__ == moduleName) and ((memObj.__name__ == memName))):
                    td = main.getTd(memObj.__module__,memObj.__name__)
                    members1 = None
                    try:
                        members1 = inspect_Inspect_Module.getmembers(memObj)
                    except BaseException as _g1:
                        None
                        haxe_Log.trace(((("cannot getmembers of " + ("null" if moduleName is None else moduleName)) + " ") + ("null" if memName is None else memName)),_hx_AnonObject({'fileName': "src/pyextern/Processor.hx", 'lineNumber': 196, 'className': "pyextern.Processor", 'methodName': "processModule"}))
                        continue
                    _g2 = 0
                    while (_g2 < len(members1)):
                        clsMem = (members1[_g2] if _g2 >= 0 and _g2 < len(members1) else None)
                        _g2 = (_g2 + 1)
                        clsMemName = clsMem[0]
                        clsMemObj = clsMem[1]
                        if self.isMethod(clsMemObj):
                            sig = None
                            try:
                                sig = inspect_Inspect_Module.signature(clsMemObj)
                            except BaseException as _g3:
                                None
                                sig = None
                            baseFunction = [None]
                            def _hx_local_5(baseFunction):
                                def _hx_local_4(cls,funcName):
                                    _hx_dict = Reflect.field(cls,"__dict__")
                                    if (funcName in _hx_dict):
                                        return _hx_dict.get(funcName)
                                    else:
                                        mro = Reflect.field(cls,"__mro__")
                                        if (len(mro) > 1):
                                            return (baseFunction[0] if 0 < len(baseFunction) else None)(mro[1],funcName)
                                        else:
                                            return None
                                return _hx_local_4
                            python_internal_ArrayImpl._set(baseFunction, 0, _hx_local_5(baseFunction))
                            typeName = Reflect.field(self.type((baseFunction[0] if 0 < len(baseFunction) else None)(memObj,clsMemName)),"__name__")
                            fun = self.sigToFun(sig,inspect_Inspect_Module.getdoc(clsMemObj))
                            isStaticMethod = self.isMethodStatic(typeName,clsMemName,clsMemObj,fun)
                            if (fun is not None):
                                if (not isStaticMethod):
                                    if (len(fun.args) < 1):
                                        haxe_Log.trace(((((("null" if moduleName is None else moduleName) + " ") + ("null" if memName is None else memName)) + " ") + ("null" if clsMemName is None else clsMemName)),_hx_AnonObject({'fileName': "src/pyextern/Processor.hx", 'lineNumber': 231, 'className': "pyextern.Processor", 'methodName': "processModule"}))
                                        haxe_Log.trace(typeName,_hx_AnonObject({'fileName': "src/pyextern/Processor.hx", 'lineNumber': 232, 'className': "pyextern.Processor", 'methodName': "processModule"}))
                                        haxe_Log.trace(sig,_hx_AnonObject({'fileName': "src/pyextern/Processor.hx", 'lineNumber': 233, 'className': "pyextern.Processor", 'methodName': "processModule"}))
                                        haxe_Log.trace("isInstanceMethod but no argument?",_hx_AnonObject({'fileName': "src/pyextern/Processor.hx", 'lineNumber': 234, 'className': "pyextern.Processor", 'methodName': "processModule"}))
                                    else:
                                        fun1 = ((fun.args[0] if 0 < len(fun.args) else None).name != "self")
                                    _this = fun.args
                                    if (len(_this) != 0):
                                        _this.pop(0)
                                elif (((typeName != "staticmethod") and ((len(fun.args) > 0))) and (((fun.args[0] if 0 < len(fun.args) else None).name == "self"))):
                                    haxe_Log.trace(clsMemName,_hx_AnonObject({'fileName': "src/pyextern/Processor.hx", 'lineNumber': 249, 'className': "pyextern.Processor", 'methodName': "processModule"}))
                                    haxe_Log.trace(typeName,_hx_AnonObject({'fileName': "src/pyextern/Processor.hx", 'lineNumber': 250, 'className': "pyextern.Processor", 'methodName': "processModule"}))
                                    raise haxe_Exception.thrown("not isInstanceMethod but has self arguement?")
                            else:
                                fun = _hx_AnonObject({'params': [], 'args': [_hx_AnonObject({'opt': False, 'name': "args", 'type': haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': ["haxe", "extern"], 'name': "Rest", 'params': [haxe_macro_TypeParam.TPType(haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Dynamic", 'params': []})))]}))})], 'ret': haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Dynamic", 'params': []})), 'expr': None})
                            field = [_hx_AnonObject({'doc': self.getdoc(clsMemObj), 'meta': [], 'access': ([haxe_macro_Access.AStatic, haxe_macro_Access.APublic] if isStaticMethod else [haxe_macro_Access.APublic]), 'name': clsMemName, 'kind': haxe_macro_FieldType.FFun(fun), 'pos': None})]
                            if pyextern_Main.isHxKeyword(clsMemName):
                                (field[0] if 0 < len(field) else None).name = ("_" + ("null" if clsMemName is None else clsMemName))
                                _this1 = Reflect.field((field[0] if 0 < len(field) else None),"meta")
                                _this1.append(_hx_AnonObject({'name': ":native", 'params': [_hx_AnonObject({'expr': haxe_macro_ExprDef.EConst(haxe_macro_Constant.CString(clsMemName)), 'pos': None})], 'pos': None}))
                            def _hx_local_7(field):
                                def _hx_local_6(f):
                                    return (f.name == (field[0] if 0 < len(field) else None).name)
                                return _hx_local_6
                            if (not Lambda.exists(td.fields,_hx_local_7(field))):
                                _this2 = td.fields
                                _this2.append((field[0] if 0 < len(field) else None))
                                if (clsMemName == "__init__"):
                                    field_new = Reflect.copy((field[0] if 0 < len(field) else None))
                                    field_new.name = "new"
                                    Reflect.setField(field_new,"meta",[])
                                    _g4 = field_new.kind
                                    tmp = None
                                    if (_g4.index == 1):
                                        f = _g4.params[0]
                                        f_new = Reflect.copy(f)
                                        Reflect.setField(f_new,"ret",haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Void", 'params': []})))
                                        tmp = haxe_macro_FieldType.FFun(f_new)
                                    else:
                                        raise haxe_Exception.thrown("should be FFun")
                                    field_new.kind = tmp
                                    _this3 = td.fields
                                    _this3.append(field_new)
                        else:
                            isInstanceField = (not self.isFieldStatic(clsMemObj))
                            doc = self.getdoc(clsMemObj)
                            _g5 = self.docReturns(doc)
                            field1 = None
                            if (_g5 is None):
                                field1 = haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Dynamic", 'params': []}))
                            else:
                                ret = _g5
                                field1 = ret
                            field2 = [_hx_AnonObject({'doc': doc, 'meta': [], 'access': ([haxe_macro_Access.APublic] if isInstanceField else [haxe_macro_Access.AStatic, haxe_macro_Access.APublic]), 'name': clsMemName, 'kind': haxe_macro_FieldType.FVar(field1), 'pos': None})]
                            if pyextern_Main.isHxKeyword(clsMemName):
                                (field2[0] if 0 < len(field2) else None).name = ("_" + ("null" if clsMemName is None else clsMemName))
                                _this4 = Reflect.field((field2[0] if 0 < len(field2) else None),"meta")
                                _this4.append(_hx_AnonObject({'name': ":native", 'params': [_hx_AnonObject({'expr': haxe_macro_ExprDef.EConst(haxe_macro_Constant.CString(clsMemName)), 'pos': None})], 'pos': None}))
                            def _hx_local_9(field):
                                def _hx_local_8(f):
                                    return (f.name == (field[0] if 0 < len(field) else None).name)
                                return _hx_local_8
                            if (not Lambda.exists(td.fields,_hx_local_9(field2))):
                                _this5 = td.fields
                                _this5.append((field2[0] if 0 < len(field2) else None))
                else:
                    try:
                        if main.filterModules(memObj.__module__):
                            real_td = main.getTd(memObj.__module__,memObj.__name__)
                            td1 = main.getTd(moduleName,memName)
                            _this6 = td1.pack
                            tmp1 = ".".join([python_Boot.toString1(x1,'') for x1 in _this6])
                            _this7 = real_td.pack
                            if ((tmp1 == ".".join([python_Boot.toString1(x1,'') for x1 in _this7])) and ((td1.name == real_td.name))):
                                raise haxe_Exception.thrown("typedef of itself?")
                            Reflect.setField(td1,"meta",[])
                            Reflect.setField(td1,"isExtern",False)
                            td1.kind = haxe_macro_TypeDefKind.TDAlias(haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': real_td.pack, 'name': real_td.name})))
                    except BaseException as _g6:
                        None
            else:
                td2 = main.getTd(moduleName,"")
                _this8 = pyextern_Main.re_ident
                _this8.matchObj = python_lib_Re.search(_this8.pattern,memName)
                if (_this8.matchObj is None):
                    raise haxe_Exception.thrown(memName)
                if self.isMethod(memObj):
                    sig1 = None
                    try:
                        sig1 = (inspect_Inspect_Module.signature(memObj) if ((memName != "group_cumsum")) else None)
                    except BaseException as _g7:
                        None
                        sig1 = None
                    fun2 = (self.sigToFun(sig1,inspect_Inspect_Module.getdoc(memObj)) if ((sig1 is not None)) else _hx_AnonObject({'params': [], 'args': [_hx_AnonObject({'opt': False, 'name': "args", 'type': haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': ["haxe", "extern"], 'name': "Rest", 'params': [haxe_macro_TypeParam.TPType(haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Dynamic", 'params': []})))]}))})], 'ret': haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Dynamic", 'params': []})), 'expr': None}))
                    field3 = [_hx_AnonObject({'doc': self.getdoc(memObj), 'meta': [], 'access': [haxe_macro_Access.AStatic, haxe_macro_Access.APublic], 'name': memName, 'kind': haxe_macro_FieldType.FFun(fun2), 'pos': None})]
                    if pyextern_Main.isHxKeyword(memName):
                        (field3[0] if 0 < len(field3) else None).name = ("_" + ("null" if memName is None else memName))
                        _this9 = Reflect.field((field3[0] if 0 < len(field3) else None),"meta")
                        _this9.append(_hx_AnonObject({'name': ":native", 'params': [_hx_AnonObject({'expr': haxe_macro_ExprDef.EConst(haxe_macro_Constant.CString(memName)), 'pos': None})], 'pos': None}))
                    def _hx_local_11(field):
                        def _hx_local_10(f):
                            return (f.name == (field[0] if 0 < len(field) else None).name)
                        return _hx_local_10
                    if (not Lambda.exists(td2.fields,_hx_local_11(field3))):
                        _this10 = td2.fields
                        _this10.append((field3[0] if 0 < len(field3) else None))
                else:
                    doc1 = self.getdoc(memObj)
                    _g8 = self.docReturns(doc1)
                    field4 = None
                    if (_g8 is None):
                        field4 = haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Dynamic", 'params': []}))
                    else:
                        ret1 = _g8
                        field4 = ret1
                    field5 = [_hx_AnonObject({'doc': doc1, 'meta': [], 'access': [haxe_macro_Access.AStatic, haxe_macro_Access.APublic], 'name': memName, 'kind': haxe_macro_FieldType.FVar(field4), 'pos': None})]
                    if pyextern_Main.isHxKeyword(memName):
                        (field5[0] if 0 < len(field5) else None).name = ("_" + ("null" if memName is None else memName))
                        _this11 = Reflect.field((field5[0] if 0 < len(field5) else None),"meta")
                        _this11.append(_hx_AnonObject({'name': ":native", 'params': [_hx_AnonObject({'expr': haxe_macro_ExprDef.EConst(haxe_macro_Constant.CString(memName)), 'pos': None})], 'pos': None}))
                    def _hx_local_13(field):
                        def _hx_local_12(f):
                            return (f.name == (field[0] if 0 < len(field) else None).name)
                        return _hx_local_12
                    if (not Lambda.exists(td2.fields,_hx_local_13(field5))):
                        _this12 = td2.fields
                        _this12.append((field5[0] if 0 < len(field5) else None))

    def hxType(self,_hx_type):
        type1 = _hx_type
        _hx_local_0 = len(type1)
        if (_hx_local_0 == 9):
            if (type1 == "generator"):
                return haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': ["python"], 'name': "NativeIterable", 'params': [haxe_macro_TypeParam.TPType(haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Dynamic", 'params': []})))]}))
            else:
                other = _hx_type
                return None
        elif (_hx_local_0 == 5):
            if (type1 == "array"):
                return haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Array", 'params': [haxe_macro_TypeParam.TPType(haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Dynamic", 'params': []})))]}))
            elif (type1 == "float"):
                return haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Float", 'params': []}))
            elif (type1 == "tuple"):
                return haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': ["python"], 'name': "Tuple", 'params': [haxe_macro_TypeParam.TPType(haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Dynamic", 'params': []})))]}))
            else:
                other = _hx_type
                return None
        elif (_hx_local_0 == 4):
            if (type1 == "bool"):
                return haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Bool", 'params': []}))
            elif (type1 == "dict"):
                return haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': ["python"], 'name': "Dict", 'params': [haxe_macro_TypeParam.TPType(haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Dynamic", 'params': []}))), haxe_macro_TypeParam.TPType(haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Dynamic", 'params': []})))]}))
            elif (type1 == "list"):
                return haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Array", 'params': [haxe_macro_TypeParam.TPType(haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Dynamic", 'params': []})))]}))
            else:
                other = _hx_type
                return None
        elif (_hx_local_0 == 13):
            if (type1 == "Python object"):
                return haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Dynamic", 'params': []}))
            else:
                other = _hx_type
                return None
        elif (_hx_local_0 == 3):
            if (type1 == "any"):
                return haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Dynamic", 'params': []}))
            elif (type1 == "int"):
                return haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Int", 'params': []}))
            elif (type1 == "str"):
                return haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "String", 'params': []}))
            else:
                other = _hx_type
                return None
        elif (_hx_local_0 == 8):
            if (type1 == "callable"):
                return haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': ["haxe"], 'name': "Constraints", 'params': [], 'sub': "Function"}))
            elif (type1 == "function"):
                return haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': ["haxe"], 'name': "Constraints", 'params': [], 'sub': "Function"}))
            else:
                other = _hx_type
                return None
        elif (_hx_local_0 == 6):
            if (type1 == "object"):
                return haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Dynamic", 'params': []}))
            elif (type1 == "string"):
                return haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "String", 'params': []}))
            else:
                other = _hx_type
                return None
        else:
            other = _hx_type
            return None

    def hxVal(self,v):
        _hx_tmp = None
        if (v is None):
            return haxe_ds_Option._hx_None
        else:
            v1 = v
            _hx_local_0 = len(v1)
            if (_hx_local_0 == 5):
                if (v1 == "False"):
                    return haxe_ds_Option.Some(_hx_AnonObject({'expr': haxe_macro_ExprDef.EConst(haxe_macro_Constant.CIdent("false")), 'pos': _hx_AnonObject({'file': "src/pyextern/Processor.hx", 'min': 13268, 'max': 13273})}))
                else:
                    _this = EReg("^<class '(.+)'>$","")
                    _this.matchObj = python_lib_Re.search(_this.pattern,v)
                    _hx_tmp = (_this.matchObj is not None)
                    v = _hx_tmp
                    return haxe_ds_Option.Some(None)
            elif (_hx_local_0 == 4):
                if (v1 == "None"):
                    return haxe_ds_Option.Some(_hx_AnonObject({'expr': haxe_macro_ExprDef.EConst(haxe_macro_Constant.CIdent("null")), 'pos': _hx_AnonObject({'file': "src/pyextern/Processor.hx", 'min': 13191, 'max': 13195})}))
                elif (v1 == "True"):
                    return haxe_ds_Option.Some(_hx_AnonObject({'expr': haxe_macro_ExprDef.EConst(haxe_macro_Constant.CIdent("true")), 'pos': _hx_AnonObject({'file': "src/pyextern/Processor.hx", 'min': 13229, 'max': 13233})}))
                else:
                    _this = EReg("^<class '(.+)'>$","")
                    _this.matchObj = python_lib_Re.search(_this.pattern,v)
                    _hx_tmp = (_this.matchObj is not None)
                    v = _hx_tmp
                    return haxe_ds_Option.Some(None)
            elif (_hx_local_0 == 24):
                if (v1 == "<built-in function repr>"):
                    return haxe_ds_Option.Some(_hx_AnonObject({'expr': haxe_macro_ExprDef.EField(_hx_AnonObject({'expr': haxe_macro_ExprDef.EField(_hx_AnonObject({'expr': haxe_macro_ExprDef.EConst(haxe_macro_Constant.CIdent("haxe")), 'pos': _hx_AnonObject({'file': "src/pyextern/Processor.hx", 'min': 13327, 'max': 13331})}),"Constraints"), 'pos': _hx_AnonObject({'file': "src/pyextern/Processor.hx", 'min': 13327, 'max': 13343})}),"Function"), 'pos': _hx_AnonObject({'file': "src/pyextern/Processor.hx", 'min': 13327, 'max': 13352})}))
                else:
                    _this = EReg("^<class '(.+)'>$","")
                    _this.matchObj = python_lib_Re.search(_this.pattern,v)
                    _hx_tmp = (_this.matchObj is not None)
                    v = _hx_tmp
                    return haxe_ds_Option.Some(None)
            else:
                _this = EReg("^<class '(.+)'>$","")
                _this.matchObj = python_lib_Re.search(_this.pattern,v)
                _hx_tmp = (_this.matchObj is not None)
                v = _hx_tmp
                return haxe_ds_Option.Some(None)

    @staticmethod
    def docDefaults():
        p = docutils_frontend_OptionParser([docutils_parsers_rst_Parser])
        v = p.get_default_values()
        v.report_level = 5
        return v

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.currentModule = None
pyextern_Processor._hx_class = pyextern_Processor
_hx_classes["pyextern.Processor"] = pyextern_Processor


class pyextern_Process_numpy(pyextern_Processor):
    _hx_class_name = "pyextern.Process_numpy"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["hxType"]
    _hx_statics = ["__meta__"]
    _hx_interfaces = []
    _hx_super = pyextern_Processor


    def __init__(self):
        super().__init__()

    def hxType(self,_hx_type):
        _g = super().hxType(_hx_type)
        if (_g is None):
            type1 = _hx_type
            _hx_local_0 = len(type1)
            if (_hx_local_0 == 10):
                if (type1 == "array_like"):
                    return haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': ["python"], 'name': "NativeIterable", 'params': [haxe_macro_TypeParam.TPType(haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Dynamic", 'params': []})))]}))
                else:
                    other = _hx_type
                    curCls = Type.getClassName(Type.getClass(self))
                    haxe_Log.trace(((((("" + ("null" if curCls is None else curCls)) + ".hxType not able to handle: ") + HxOverrides.stringOrNull(self.currentModule)) + " ") + ("null" if other is None else other)),_hx_AnonObject({'fileName': "src/pyextern/Processor_numpy.hx", 'lineNumber': 27, 'className': "pyextern.Process_numpy", 'methodName': "hxType"}))
                    return None
            elif (_hx_local_0 == 11):
                if (type1 == "MaskedArray"):
                    return haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': ["numpy", "ma"], 'name': "MaskedArray", 'params': []}))
                else:
                    other = _hx_type
                    curCls = Type.getClassName(Type.getClass(self))
                    haxe_Log.trace(((((("" + ("null" if curCls is None else curCls)) + ".hxType not able to handle: ") + HxOverrides.stringOrNull(self.currentModule)) + " ") + ("null" if other is None else other)),_hx_AnonObject({'fileName': "src/pyextern/Processor_numpy.hx", 'lineNumber': 27, 'className': "pyextern.Process_numpy", 'methodName': "hxType"}))
                    return None
            elif (_hx_local_0 == 7):
                if (type1 == "ndarray"):
                    return haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': ["numpy"], 'name': "Ndarray", 'params': []}))
                else:
                    other = _hx_type
                    curCls = Type.getClassName(Type.getClass(self))
                    haxe_Log.trace(((((("" + ("null" if curCls is None else curCls)) + ".hxType not able to handle: ") + HxOverrides.stringOrNull(self.currentModule)) + " ") + ("null" if other is None else other)),_hx_AnonObject({'fileName': "src/pyextern/Processor_numpy.hx", 'lineNumber': 27, 'className': "pyextern.Process_numpy", 'methodName': "hxType"}))
                    return None
            elif (_hx_local_0 == 6):
                if (type1 == "matrix"):
                    return haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': ["numpy"], 'name': "Matrix", 'params': []}))
                elif (type1 == "scalar"):
                    return haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Dynamic", 'params': []}))
                else:
                    other = _hx_type
                    curCls = Type.getClassName(Type.getClass(self))
                    haxe_Log.trace(((((("" + ("null" if curCls is None else curCls)) + ".hxType not able to handle: ") + HxOverrides.stringOrNull(self.currentModule)) + " ") + ("null" if other is None else other)),_hx_AnonObject({'fileName': "src/pyextern/Processor_numpy.hx", 'lineNumber': 27, 'className': "pyextern.Process_numpy", 'methodName': "hxType"}))
                    return None
            else:
                other = _hx_type
                curCls = Type.getClassName(Type.getClass(self))
                haxe_Log.trace(((((("" + ("null" if curCls is None else curCls)) + ".hxType not able to handle: ") + HxOverrides.stringOrNull(self.currentModule)) + " ") + ("null" if other is None else other)),_hx_AnonObject({'fileName': "src/pyextern/Processor_numpy.hx", 'lineNumber': 27, 'className': "pyextern.Process_numpy", 'methodName': "hxType"}))
                return None
        else:
            ct = _g
            return ct

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
pyextern_Process_numpy._hx_class = pyextern_Process_numpy
_hx_classes["pyextern.Process_numpy"] = pyextern_Process_numpy


class pyextern_Process_pandas(pyextern_Processor):
    _hx_class_name = "pyextern.Process_pandas"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["hxType"]
    _hx_statics = ["__meta__", "classes", "get_classes"]
    _hx_interfaces = []
    _hx_super = pyextern_Processor


    def __init__(self):
        super().__init__()

    def hxType(self,_hx_type):
        _g = super().hxType(_hx_type)
        if (_g is None):
            type1 = _hx_type
            _hx_local_0 = len(type1)
            if (_hx_local_0 == 7):
                if (type1 == "NDFrame"):
                    return haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': ["pandas", "core", "frame"], 'name': "NDFrame", 'params': []}))
                elif (type1 == "ndarray"):
                    return haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': ["numpy"], 'name': "Ndarray", 'params': []}))
                elif (_hx_type in pyextern_Process_pandas.get_classes().h):
                    return haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': ["pandas"], 'name': _hx_type}))
                else:
                    other = _hx_type
                    curCls = Type.getClassName(Type.getClass(self))
                    haxe_Log.trace(((((("" + ("null" if curCls is None else curCls)) + ".hxType not able to handle: ") + HxOverrides.stringOrNull(self.currentModule)) + " ") + ("null" if other is None else other)),_hx_AnonObject({'fileName': "src/pyextern/Processor_pandas.hx", 'lineNumber': 32, 'className': "pyextern.Process_pandas", 'methodName': "hxType"}))
                    return None
            elif (_hx_local_0 == 8):
                if (type1 == "pd.Index"):
                    return haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': ["pandas"], 'name': "Index", 'params': []}))
                elif (_hx_type in pyextern_Process_pandas.get_classes().h):
                    return haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': ["pandas"], 'name': _hx_type}))
                else:
                    other = _hx_type
                    curCls = Type.getClassName(Type.getClass(self))
                    haxe_Log.trace(((((("" + ("null" if curCls is None else curCls)) + ".hxType not able to handle: ") + HxOverrides.stringOrNull(self.currentModule)) + " ") + ("null" if other is None else other)),_hx_AnonObject({'fileName': "src/pyextern/Processor_pandas.hx", 'lineNumber': 32, 'className': "pyextern.Process_pandas", 'methodName': "hxType"}))
                    return None
            elif (_hx_type in pyextern_Process_pandas.get_classes().h):
                return haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': ["pandas"], 'name': _hx_type}))
            else:
                other = _hx_type
                curCls = Type.getClassName(Type.getClass(self))
                haxe_Log.trace(((((("" + ("null" if curCls is None else curCls)) + ".hxType not able to handle: ") + HxOverrides.stringOrNull(self.currentModule)) + " ") + ("null" if other is None else other)),_hx_AnonObject({'fileName': "src/pyextern/Processor_pandas.hx", 'lineNumber': 32, 'className': "pyextern.Process_pandas", 'methodName': "hxType"}))
                return None
        else:
            ct = _g
            return ct
    classes = None

    @staticmethod
    def get_classes():
        if (pyextern_Process_pandas.classes is not None):
            return pyextern_Process_pandas.classes
        else:
            module = importlib_Importlib_Module.import_module("pandas")
            _g = haxe_ds_StringMap()
            _g1 = 0
            _g2 = inspect_Inspect_Module.getmembers(module,inspect_Inspect_Module.isclass)
            while (_g1 < len(_g2)):
                clsTp = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
                _g1 = (_g1 + 1)
                _g.h[clsTp[0]] = True
            def _hx_local_2():
                def _hx_local_1():
                    pyextern_Process_pandas.classes = _g
                    return pyextern_Process_pandas.classes
                return _hx_local_1()
            return _hx_local_2()

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
pyextern_Process_pandas._hx_class = pyextern_Process_pandas
_hx_classes["pyextern.Process_pandas"] = pyextern_Process_pandas


class pyextern_Process_pyqt5(pyextern_Processor):
    _hx_class_name = "pyextern.Process_pyqt5"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["isMethod", "isFieldStatic", "sigToFun"]
    _hx_statics = ["__meta__", "removeBrackets"]
    _hx_interfaces = []
    _hx_super = pyextern_Processor


    def __init__(self):
        super().__init__()

    def isMethod(self,memObj):
        doc = inspect_Inspect_Module.getdoc(memObj)
        if ((doc is not None) and doc.endswith(" [signal]")):
            return False
        return super().isMethod(memObj)

    def isFieldStatic(self,memObj):
        doc = inspect_Inspect_Module.getdoc(memObj)
        if ((doc is not None) and doc.endswith(" [signal]")):
            return False
        return super().isFieldStatic(memObj)

    def sigToFun(self,sig,doc):
        _gthis = self
        if ((sig is None) and ((doc is not None))):
            docLines = doc.split("\n")
            funcR = EReg("^(.+?)\\((.*)\\)(?:\\s*->\\s*(.+))?$","")
            if ((len(docLines) > 0) and Lambda.foreach(docLines,funcR.match)):
                _g = []
                _g1 = 0
                while (_g1 < len(docLines)):
                    doc1 = (docLines[_g1] if _g1 >= 0 and _g1 < len(docLines) else None)
                    _g1 = (_g1 + 1)
                    funcR.matchObj = python_lib_Re.search(funcR.pattern,doc1)
                    if (funcR.matchObj is not None):
                        funcName = funcR.matchObj.group(1)
                        funcArgs = funcR.matchObj.group(2)
                        startIndex = None
                        if (((funcArgs.find("(") if ((startIndex is None)) else HxString.indexOfImpl(funcArgs,"(",startIndex))) >= 0):
                            funcArgs = pyextern_Process_pyqt5.removeBrackets(funcArgs,"(",")")
                        startIndex1 = None
                        if (((funcArgs.find("[") if ((startIndex1 is None)) else HxString.indexOfImpl(funcArgs,"[",startIndex1))) >= 0):
                            funcArgs = pyextern_Process_pyqt5.removeBrackets(funcArgs,"[","]")
                        ret = funcR.matchObj.group(3)
                        def _hx_local_3():
                            def _hx_local_1(a):
                                name = None
                                _this = EReg("^[A-Za-z0-9]+$","")
                                _this.matchObj = python_lib_Re.search(_this.pattern,a)
                                if (_this.matchObj is not None):
                                    name = a
                                else:
                                    r = EReg("^[A-Za-z0-9]+","")
                                    r.matchObj = python_lib_Re.search(r.pattern,a)
                                    name = (r.matchObj.group(0) if ((r.matchObj is not None)) else "_")
                                startIndex = None
                                args = (a.find("=") if ((startIndex is None)) else HxString.indexOfImpl(a,"=",startIndex))
                                _g = _gthis.hxType(name)
                                args1 = None
                                if (_g is None):
                                    args1 = haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Dynamic", 'params': []}))
                                else:
                                    ct = _g
                                    args1 = ct
                                return _hx_AnonObject({'opt': (args >= 0), 'name': name, 'type': args1})
                            return [] if (funcArgs == "") else list(map(_hx_local_1,list(map(StringTools.trim,funcArgs.split(",")))))
                        args = _hx_local_3()
                        x = None
                        if (ret is None):
                            x = haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Void", 'params': []}))
                        else:
                            _g2 = self.hxType(ret)
                            if (_g2 is None):
                                x = haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Dynamic", 'params': []}))
                            else:
                                ct = _g2
                                x = ct
                        _g.append(_hx_AnonObject({'params': [], 'args': args, 'ret': x, 'expr': None}))
                funcs = _g
                def _hx_local_4(f,sameArgs):
                    allSame = True
                    _g = []
                    _g1 = 0
                    _g2 = len(sameArgs)
                    while (_g1 < _g2):
                        i = _g1
                        _g1 = (_g1 + 1)
                        sameArgs1 = None
                        if allSame:
                            allSame = (((i < len(f.args)) and (((f.args[i] if i >= 0 and i < len(f.args) else None).name == (sameArgs[i] if i >= 0 and i < len(sameArgs) else None).name))) and ((Reflect.field((f.args[i] if i >= 0 and i < len(f.args) else None),"opt") == Reflect.field((sameArgs[i] if i >= 0 and i < len(sameArgs) else None),"opt"))))
                            sameArgs1 = allSame
                        else:
                            sameArgs1 = False
                        if sameArgs1:
                            _g.append((sameArgs[i] if i >= 0 and i < len(sameArgs) else None))
                    return _g
                sameArgs = Lambda.fold(funcs,_hx_local_4,(funcs[0] if 0 < len(funcs) else None).args)
                def _hx_local_5(f):
                    return (len(f.args) > len(sameArgs))
                hasRest = Lambda.exists(funcs,_hx_local_5)
                def _hx_local_6(f):
                    return (haxe_macro_ComplexTypeTools.toString(f.ret) == haxe_macro_ComplexTypeTools.toString((funcs[0] if 0 < len(funcs) else None).ret))
                sameRet = Lambda.foreach(funcs,_hx_local_6)
                return _hx_AnonObject({'params': [], 'args': (sameArgs if ((not hasRest)) else (sameArgs + [_hx_AnonObject({'opt': False, 'name': "args", 'type': haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': ["haxe", "extern"], 'name': "Rest", 'params': [haxe_macro_TypeParam.TPType(haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Dynamic", 'params': []})))]}))})])), 'ret': ((funcs[0] if 0 < len(funcs) else None).ret if sameRet else haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': [], 'name': "Dynamic", 'params': []}))), 'expr': None})
        return super().sigToFun(sig,doc)

    @staticmethod
    def removeBrackets(_hx_str,open,close):
        result = ""
        opened = 0
        _g = 0
        _g1 = len(_hx_str)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            c = ("" if (((i < 0) or ((i >= len(_hx_str))))) else _hx_str[i])
            if (c == open):
                opened = (opened + 1)
            elif (c == close):
                opened = (opened - 1)
            elif (opened == 0):
                result = (("null" if result is None else result) + ("null" if c is None else c))
        return result

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
pyextern_Process_pyqt5._hx_class = pyextern_Process_pyqt5
_hx_classes["pyextern.Process_pyqt5"] = pyextern_Process_pyqt5


class pyextern_Utils:
    _hx_class_name = "pyextern.Utils"
    __slots__ = ()
    _hx_statics = ["upperCaseFirstLetter", "lowerCaseFirstLetter"]

    @staticmethod
    def upperCaseFirstLetter(_hx_str):
        re_letter = EReg("[A-Za-z]","")
        re_letter.matchObj = python_lib_Re.search(re_letter.pattern,_hx_str)
        if (re_letter.matchObj is None):
            raise haxe_Exception.thrown(("no letter in " + ("null" if _hx_str is None else _hx_str)))
        return ((HxOverrides.stringOrNull(HxString.substr(re_letter.matchObj.string,0,re_letter.matchObj.start())) + HxOverrides.stringOrNull(re_letter.matchObj.group(0).upper())) + HxOverrides.stringOrNull(HxString.substr(re_letter.matchObj.string,re_letter.matchObj.end(),None)))

    @staticmethod
    def lowerCaseFirstLetter(_hx_str):
        re_letter = EReg("[A-Za-z]","")
        re_letter.matchObj = python_lib_Re.search(re_letter.pattern,_hx_str)
        if (re_letter.matchObj is None):
            raise haxe_Exception.thrown(("no letter in " + ("null" if _hx_str is None else _hx_str)))
        return ((HxOverrides.stringOrNull(HxString.substr(re_letter.matchObj.string,0,re_letter.matchObj.start())) + HxOverrides.stringOrNull(re_letter.matchObj.group(0).lower())) + HxOverrides.stringOrNull(HxString.substr(re_letter.matchObj.string,re_letter.matchObj.end(),None)))
pyextern_Utils._hx_class = pyextern_Utils
_hx_classes["pyextern.Utils"] = pyextern_Utils


class python_Boot:
    _hx_class_name = "python.Boot"
    __slots__ = ()
    _hx_statics = ["keywords", "arrayJoin", "safeJoin", "isPyBool", "isPyInt", "isPyFloat", "isClass", "isAnonObject", "_add_dynamic", "toString", "toString1", "isMetaType", "fields", "isString", "isArray", "simpleField", "createClosure", "hasField", "field", "getInstanceFields", "getSuperClass", "getClassFields", "unsafeFastCodeAt", "handleKeywords", "prefixLength", "unhandleKeywords", "implementsInterface"]

    @staticmethod
    def arrayJoin(x,sep):
        return sep.join([python_Boot.toString1(x1,'') for x1 in x])

    @staticmethod
    def safeJoin(x,sep):
        return sep.join([x1 for x1 in x])

    @staticmethod
    def isPyBool(o):
        return isinstance(o,bool)

    @staticmethod
    def isPyInt(o):
        if isinstance(o,int):
            return (not isinstance(o,bool))
        else:
            return False

    @staticmethod
    def isPyFloat(o):
        return isinstance(o,float)

    @staticmethod
    def isClass(o):
        if (o is not None):
            if not HxOverrides.eq(o,str):
                return python_lib_Inspect.isclass(o)
            else:
                return True
        else:
            return False

    @staticmethod
    def isAnonObject(o):
        return isinstance(o,_hx_AnonObject)

    @staticmethod
    def _add_dynamic(a,b):
        if (isinstance(a,str) and isinstance(b,str)):
            return (a + b)
        if (isinstance(a,str) or isinstance(b,str)):
            return (python_Boot.toString1(a,"") + python_Boot.toString1(b,""))
        return (a + b)

    @staticmethod
    def toString(o):
        return python_Boot.toString1(o,"")

    @staticmethod
    def toString1(o,s):
        if (o is None):
            return "null"
        if isinstance(o,str):
            return o
        if (s is None):
            s = ""
        if (len(s) >= 5):
            return "<...>"
        if isinstance(o,bool):
            if o:
                return "true"
            else:
                return "false"
        if (isinstance(o,int) and (not isinstance(o,bool))):
            return str(o)
        if isinstance(o,float):
            try:
                if (o == int(o)):
                    return str(Math.floor((o + 0.5)))
                else:
                    return str(o)
            except BaseException as _g:
                None
                return str(o)
        if isinstance(o,list):
            o1 = o
            l = len(o1)
            st = "["
            s = (("null" if s is None else s) + "\t")
            _g = 0
            _g1 = l
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                prefix = ""
                if (i > 0):
                    prefix = ","
                st = (("null" if st is None else st) + HxOverrides.stringOrNull(((("null" if prefix is None else prefix) + HxOverrides.stringOrNull(python_Boot.toString1((o1[i] if i >= 0 and i < len(o1) else None),s))))))
            st = (("null" if st is None else st) + "]")
            return st
        try:
            if hasattr(o,"toString"):
                return o.toString()
        except BaseException as _g:
            None
        if hasattr(o,"__class__"):
            if isinstance(o,_hx_AnonObject):
                toStr = None
                try:
                    fields = python_Boot.fields(o)
                    _g = []
                    _g1 = 0
                    while (_g1 < len(fields)):
                        f = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                        _g1 = (_g1 + 1)
                        x = ((("" + ("null" if f is None else f)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f),(("null" if s is None else s) + "\t"))))
                        _g.append(x)
                    fieldsStr = _g
                    toStr = (("{ " + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr]))) + " }")
                except BaseException as _g:
                    None
                    return "{ ... }"
                if (toStr is None):
                    return "{ ... }"
                else:
                    return toStr
            if isinstance(o,Enum):
                o1 = o
                l = len(o1.params)
                hasParams = (l > 0)
                if hasParams:
                    paramsStr = ""
                    _g = 0
                    _g1 = l
                    while (_g < _g1):
                        i = _g
                        _g = (_g + 1)
                        prefix = ""
                        if (i > 0):
                            prefix = ","
                        paramsStr = (("null" if paramsStr is None else paramsStr) + HxOverrides.stringOrNull(((("null" if prefix is None else prefix) + HxOverrides.stringOrNull(python_Boot.toString1(o1.params[i],s))))))
                    return (((HxOverrides.stringOrNull(o1.tag) + "(") + ("null" if paramsStr is None else paramsStr)) + ")")
                else:
                    return o1.tag
            if hasattr(o,"_hx_class_name"):
                if (o.__class__.__name__ != "type"):
                    fields = python_Boot.getInstanceFields(o)
                    _g = []
                    _g1 = 0
                    while (_g1 < len(fields)):
                        f = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                        _g1 = (_g1 + 1)
                        x = ((("" + ("null" if f is None else f)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f),(("null" if s is None else s) + "\t"))))
                        _g.append(x)
                    fieldsStr = _g
                    toStr = (((HxOverrides.stringOrNull(o._hx_class_name) + "( ") + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr]))) + " )")
                    return toStr
                else:
                    fields = python_Boot.getClassFields(o)
                    _g = []
                    _g1 = 0
                    while (_g1 < len(fields)):
                        f = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                        _g1 = (_g1 + 1)
                        x = ((("" + ("null" if f is None else f)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f),(("null" if s is None else s) + "\t"))))
                        _g.append(x)
                    fieldsStr = _g
                    toStr = (((("#" + HxOverrides.stringOrNull(o._hx_class_name)) + "( ") + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr]))) + " )")
                    return toStr
            if ((type(o) == type) and (o == str)):
                return "#String"
            if ((type(o) == type) and (o == list)):
                return "#Array"
            if callable(o):
                return "function"
            try:
                if hasattr(o,"__repr__"):
                    return o.__repr__()
            except BaseException as _g:
                None
            if hasattr(o,"__str__"):
                return o.__str__([])
            if hasattr(o,"__name__"):
                return o.__name__
            return "???"
        else:
            return str(o)

    @staticmethod
    def isMetaType(v,t):
        return ((type(v) == type) and (v == t))

    @staticmethod
    def fields(o):
        a = []
        if (o is not None):
            if hasattr(o,"_hx_fields"):
                fields = o._hx_fields
                if (fields is not None):
                    return list(fields)
            if isinstance(o,_hx_AnonObject):
                d = o.__dict__
                keys = d.keys()
                handler = python_Boot.unhandleKeywords
                for k in keys:
                    if (k != '_hx_disable_getattr'):
                        a.append(handler(k))
            elif hasattr(o,"__dict__"):
                d = o.__dict__
                keys1 = d.keys()
                for k in keys1:
                    a.append(k)
        return a

    @staticmethod
    def isString(o):
        return isinstance(o,str)

    @staticmethod
    def isArray(o):
        return isinstance(o,list)

    @staticmethod
    def simpleField(o,field):
        if (field is None):
            return None
        field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
        if hasattr(o,field1):
            return getattr(o,field1)
        else:
            return None

    @staticmethod
    def createClosure(obj,func):
        return python_internal_MethodClosure(obj,func)

    @staticmethod
    def hasField(o,field):
        if isinstance(o,_hx_AnonObject):
            return o._hx_hasattr(field)
        return hasattr(o,(("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)))

    @staticmethod
    def field(o,field):
        if (field is None):
            return None
        if isinstance(o,str):
            field1 = field
            _hx_local_0 = len(field1)
            if (_hx_local_0 == 10):
                if (field1 == "charCodeAt"):
                    return python_internal_MethodClosure(o,HxString.charCodeAt)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 11):
                if (field1 == "lastIndexOf"):
                    return python_internal_MethodClosure(o,HxString.lastIndexOf)
                elif (field1 == "toLowerCase"):
                    return python_internal_MethodClosure(o,HxString.toLowerCase)
                elif (field1 == "toUpperCase"):
                    return python_internal_MethodClosure(o,HxString.toUpperCase)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 9):
                if (field1 == "substring"):
                    return python_internal_MethodClosure(o,HxString.substring)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 5):
                if (field1 == "split"):
                    return python_internal_MethodClosure(o,HxString.split)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 7):
                if (field1 == "indexOf"):
                    return python_internal_MethodClosure(o,HxString.indexOf)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 8):
                if (field1 == "toString"):
                    return python_internal_MethodClosure(o,HxString.toString)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 6):
                if (field1 == "charAt"):
                    return python_internal_MethodClosure(o,HxString.charAt)
                elif (field1 == "length"):
                    return len(o)
                elif (field1 == "substr"):
                    return python_internal_MethodClosure(o,HxString.substr)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            else:
                field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                if hasattr(o,field1):
                    return getattr(o,field1)
                else:
                    return None
        elif isinstance(o,list):
            field1 = field
            _hx_local_1 = len(field1)
            if (_hx_local_1 == 11):
                if (field1 == "lastIndexOf"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.lastIndexOf)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 4):
                if (field1 == "copy"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.copy)
                elif (field1 == "join"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.join)
                elif (field1 == "push"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.push)
                elif (field1 == "sort"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.sort)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 5):
                if (field1 == "shift"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.shift)
                elif (field1 == "slice"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.slice)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 7):
                if (field1 == "indexOf"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.indexOf)
                elif (field1 == "reverse"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.reverse)
                elif (field1 == "unshift"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.unshift)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 3):
                if (field1 == "map"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.map)
                elif (field1 == "pop"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.pop)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 8):
                if (field1 == "contains"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.contains)
                elif (field1 == "iterator"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.iterator)
                elif (field1 == "toString"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.toString)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 16):
                if (field1 == "keyValueIterator"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.keyValueIterator)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 6):
                if (field1 == "concat"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.concat)
                elif (field1 == "filter"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.filter)
                elif (field1 == "insert"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.insert)
                elif (field1 == "length"):
                    return len(o)
                elif (field1 == "remove"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.remove)
                elif (field1 == "splice"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.splice)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            else:
                field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                if hasattr(o,field1):
                    return getattr(o,field1)
                else:
                    return None
        else:
            field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
            if hasattr(o,field1):
                return getattr(o,field1)
            else:
                return None

    @staticmethod
    def getInstanceFields(c):
        f = (list(c._hx_fields) if (hasattr(c,"_hx_fields")) else [])
        if hasattr(c,"_hx_methods"):
            f = (f + c._hx_methods)
        sc = python_Boot.getSuperClass(c)
        if (sc is None):
            return f
        else:
            scArr = python_Boot.getInstanceFields(sc)
            scMap = set(scArr)
            _g = 0
            while (_g < len(f)):
                f1 = (f[_g] if _g >= 0 and _g < len(f) else None)
                _g = (_g + 1)
                if (not (f1 in scMap)):
                    scArr.append(f1)
            return scArr

    @staticmethod
    def getSuperClass(c):
        if (c is None):
            return None
        try:
            if hasattr(c,"_hx_super"):
                return c._hx_super
            return None
        except BaseException as _g:
            None
        return None

    @staticmethod
    def getClassFields(c):
        if hasattr(c,"_hx_statics"):
            x = c._hx_statics
            return list(x)
        else:
            return []

    @staticmethod
    def unsafeFastCodeAt(s,index):
        return ord(s[index])

    @staticmethod
    def handleKeywords(name):
        if (name in python_Boot.keywords):
            return ("_hx_" + name)
        elif ((((len(name) > 2) and ((ord(name[0]) == 95))) and ((ord(name[1]) == 95))) and ((ord(name[(len(name) - 1)]) != 95))):
            return ("_hx_" + name)
        else:
            return name

    @staticmethod
    def unhandleKeywords(name):
        if (HxString.substr(name,0,python_Boot.prefixLength) == "_hx_"):
            real = HxString.substr(name,python_Boot.prefixLength,None)
            if (real in python_Boot.keywords):
                return real
        return name

    @staticmethod
    def implementsInterface(value,cls):
        loop = None
        def _hx_local_1(intf):
            f = (intf._hx_interfaces if (hasattr(intf,"_hx_interfaces")) else [])
            if (f is not None):
                _g = 0
                while (_g < len(f)):
                    i = (f[_g] if _g >= 0 and _g < len(f) else None)
                    _g = (_g + 1)
                    if (i == cls):
                        return True
                    else:
                        l = loop(i)
                        if l:
                            return True
                return False
            else:
                return False
        loop = _hx_local_1
        currentClass = value.__class__
        result = False
        while (currentClass is not None):
            if loop(currentClass):
                result = True
                break
            currentClass = python_Boot.getSuperClass(currentClass)
        return result
python_Boot._hx_class = python_Boot
_hx_classes["python.Boot"] = python_Boot


class python_HaxeIterable:
    _hx_class_name = "python.HaxeIterable"
    __slots__ = ("x",)
    _hx_fields = ["x"]
    _hx_methods = ["iterator"]

    def __init__(self,x):
        self.x = x

    def iterator(self):
        return python_HaxeIterator(self.x.__iter__())

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.x = None
python_HaxeIterable._hx_class = python_HaxeIterable
_hx_classes["python.HaxeIterable"] = python_HaxeIterable


class python_HaxeIterator:
    _hx_class_name = "python.HaxeIterator"
    __slots__ = ("it", "x", "has", "checked")
    _hx_fields = ["it", "x", "has", "checked"]
    _hx_methods = ["next", "hasNext"]

    def __init__(self,it):
        self.checked = False
        self.has = False
        self.x = None
        self.it = it

    def next(self):
        if (not self.checked):
            self.hasNext()
        self.checked = False
        return self.x

    def hasNext(self):
        if (not self.checked):
            try:
                self.x = self.it.__next__()
                self.has = True
            except BaseException as _g:
                None
                if Std.isOfType(haxe_Exception.caught(_g).unwrap(),StopIteration):
                    self.has = False
                    self.x = None
                else:
                    raise _g
            self.checked = True
        return self.has

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.it = None
        _hx_o.x = None
        _hx_o.has = None
        _hx_o.checked = None
python_HaxeIterator._hx_class = python_HaxeIterator
_hx_classes["python.HaxeIterator"] = python_HaxeIterator


class python__KwArgs_KwArgs_Impl_:
    _hx_class_name = "python._KwArgs.KwArgs_Impl_"
    __slots__ = ()
    _hx_statics = ["_new", "toDict", "toDictHelper", "fromDict", "fromT", "typed", "get"]

    @staticmethod
    def _new(d):
        this1 = d
        return this1

    @staticmethod
    def toDict(this1):
        return python__KwArgs_KwArgs_Impl_.toDictHelper(this1,None)

    @staticmethod
    def toDictHelper(this1,x):
        return this1

    @staticmethod
    def fromDict(d):
        this1 = d
        return this1

    @staticmethod
    def fromT(d):
        this1 = python_Lib.anonAsDict(d)
        return this1

    @staticmethod
    def typed(this1):
        return _hx_AnonObject(python__KwArgs_KwArgs_Impl_.toDictHelper(this1,None))

    @staticmethod
    def get(this1,key,_hx_def):
        return this1.get(key,_hx_def)
python__KwArgs_KwArgs_Impl_._hx_class = python__KwArgs_KwArgs_Impl_
_hx_classes["python._KwArgs.KwArgs_Impl_"] = python__KwArgs_KwArgs_Impl_


class python_Lib:
    _hx_class_name = "python.Lib"
    __slots__ = ()
    _hx_statics = ["lineEnd", "get___name__", "print", "printString", "println", "dictToAnon", "anonToDict", "anonAsDict", "dictAsAnon", "toPythonIterable", "toHaxeIterable", "toHaxeIterator"]
    __name__ = None

    @staticmethod
    def get___name__():
        return __name__

    @staticmethod
    def print(v):
        python_Lib.printString(Std.string(v))

    @staticmethod
    def printString(_hx_str):
        encoding = "utf-8"
        if (encoding is None):
            encoding = "utf-8"
        python_lib_Sys.stdout.buffer.write(_hx_str.encode(encoding, "strict"))
        python_lib_Sys.stdout.flush()

    @staticmethod
    def println(v):
        _hx_str = Std.string(v)
        python_Lib.printString((("" + ("null" if _hx_str is None else _hx_str)) + HxOverrides.stringOrNull(python_Lib.lineEnd)))

    @staticmethod
    def dictToAnon(v):
        return _hx_AnonObject(v.copy())

    @staticmethod
    def anonToDict(o):
        if isinstance(o,_hx_AnonObject):
            return o.__dict__.copy()
        else:
            return None

    @staticmethod
    def anonAsDict(o):
        if isinstance(o,_hx_AnonObject):
            return o.__dict__
        else:
            return None

    @staticmethod
    def dictAsAnon(d):
        return _hx_AnonObject(d)

    @staticmethod
    def toPythonIterable(it):
        def _hx_local_3():
            def _hx_local_2():
                it1 = HxOverrides.iterator(it)
                _hx_self = None
                def _hx_local_0():
                    if it1.hasNext():
                        return it1.next()
                    else:
                        raise haxe_Exception.thrown(StopIteration())
                def _hx_local_1():
                    return _hx_self
                this1 = _hx_AnonObject({'__next__': _hx_local_0, '__iter__': _hx_local_1})
                _hx_self = this1
                return _hx_self
            return _hx_AnonObject({'__iter__': _hx_local_2})
        return _hx_local_3()

    @staticmethod
    def toHaxeIterable(it):
        return python_HaxeIterable(it)

    @staticmethod
    def toHaxeIterator(it):
        return python_HaxeIterator(it)
python_Lib._hx_class = python_Lib
_hx_classes["python.Lib"] = python_Lib


class python__NativeIterable_NativeIterable_Impl_:
    _hx_class_name = "python._NativeIterable.NativeIterable_Impl_"
    __slots__ = ()
    _hx_statics = ["toHaxeIterable", "iterator"]

    @staticmethod
    def toHaxeIterable(this1):
        return python_HaxeIterable(this1)

    @staticmethod
    def iterator(this1):
        return python_HaxeIterator(this1.__iter__())
python__NativeIterable_NativeIterable_Impl_._hx_class = python__NativeIterable_NativeIterable_Impl_
_hx_classes["python._NativeIterable.NativeIterable_Impl_"] = python__NativeIterable_NativeIterable_Impl_


class python__NativeIterator_NativeIterator_Impl_:
    _hx_class_name = "python._NativeIterator.NativeIterator_Impl_"
    __slots__ = ()
    _hx_statics = ["_new", "toHaxeIterator"]

    @staticmethod
    def _new(p):
        this1 = p
        return this1

    @staticmethod
    def toHaxeIterator(this1):
        return python_HaxeIterator(this1)
python__NativeIterator_NativeIterator_Impl_._hx_class = python__NativeIterator_NativeIterator_Impl_
_hx_classes["python._NativeIterator.NativeIterator_Impl_"] = python__NativeIterator_NativeIterator_Impl_


class python_NativeStringTools:
    _hx_class_name = "python.NativeStringTools"
    __slots__ = ()
    _hx_statics = ["format", "encode", "contains", "strip", "rpartition", "startswith", "endswith"]

    @staticmethod
    def format(s,args):
        return s.format(*args)

    @staticmethod
    def encode(s,encoding = None,errors = None):
        if (encoding is None):
            encoding = "utf-8"
        if (errors is None):
            errors = "strict"
        return s.encode(encoding, errors)

    @staticmethod
    def contains(s,e):
        return (e in s)

    @staticmethod
    def strip(s,chars = None):
        return s.strip(chars)

    @staticmethod
    def rpartition(s,sep):
        return s.rpartition(sep)

    @staticmethod
    def startswith(s,prefix):
        return s.startswith(prefix)

    @staticmethod
    def endswith(s,suffix):
        return s.endswith(suffix)
python_NativeStringTools._hx_class = python_NativeStringTools
_hx_classes["python.NativeStringTools"] = python_NativeStringTools


class python__VarArgs_VarArgs_Impl_:
    _hx_class_name = "python._VarArgs.VarArgs_Impl_"
    __slots__ = ()
    _hx_statics = ["_new", "raw", "toArray", "fromArray"]

    @staticmethod
    def _new(d):
        this1 = d
        return this1

    @staticmethod
    def raw(this1):
        return this1

    @staticmethod
    def toArray(this1):
        if (not Std.isOfType(this1,list)):
            return list(this1)
        else:
            return this1

    @staticmethod
    def fromArray(d):
        this1 = d
        return this1
python__VarArgs_VarArgs_Impl_._hx_class = python__VarArgs_VarArgs_Impl_
_hx_classes["python._VarArgs.VarArgs_Impl_"] = python__VarArgs_VarArgs_Impl_


class python_internal_ArrayImpl:
    _hx_class_name = "python.internal.ArrayImpl"
    __slots__ = ()
    _hx_statics = ["get_length", "concat", "copy", "iterator", "keyValueIterator", "indexOf", "lastIndexOf", "join", "toString", "pop", "push", "unshift", "remove", "contains", "shift", "slice", "sort", "splice", "map", "filter", "insert", "reverse", "_get", "_set", "unsafeGet", "unsafeSet", "resize"]

    @staticmethod
    def get_length(x):
        return len(x)

    @staticmethod
    def concat(a1,a2):
        return (a1 + a2)

    @staticmethod
    def copy(x):
        return list(x)

    @staticmethod
    def iterator(x):
        return python_HaxeIterator(x.__iter__())

    @staticmethod
    def keyValueIterator(x):
        return haxe_iterators_ArrayKeyValueIterator(x)

    @staticmethod
    def indexOf(a,x,fromIndex = None):
        _hx_len = len(a)
        l = (0 if ((fromIndex is None)) else ((_hx_len + fromIndex) if ((fromIndex < 0)) else fromIndex))
        if (l < 0):
            l = 0
        _g = l
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if HxOverrides.eq(a[i],x):
                return i
        return -1

    @staticmethod
    def lastIndexOf(a,x,fromIndex = None):
        _hx_len = len(a)
        l = (_hx_len if ((fromIndex is None)) else (((_hx_len + fromIndex) + 1) if ((fromIndex < 0)) else (fromIndex + 1)))
        if (l > _hx_len):
            l = _hx_len
        while True:
            l = (l - 1)
            tmp = l
            if (not ((tmp > -1))):
                break
            if HxOverrides.eq(a[l],x):
                return l
        return -1

    @staticmethod
    def join(x,sep):
        return sep.join([python_Boot.toString1(x1,'') for x1 in x])

    @staticmethod
    def toString(x):
        return (("[" + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in x]))) + "]")

    @staticmethod
    def pop(x):
        if (len(x) == 0):
            return None
        else:
            return x.pop()

    @staticmethod
    def push(x,e):
        x.append(e)
        return len(x)

    @staticmethod
    def unshift(x,e):
        x.insert(0, e)

    @staticmethod
    def remove(x,e):
        try:
            x.remove(e)
            return True
        except BaseException as _g:
            None
            return False

    @staticmethod
    def contains(x,e):
        return (e in x)

    @staticmethod
    def shift(x):
        if (len(x) == 0):
            return None
        return x.pop(0)

    @staticmethod
    def slice(x,pos,end = None):
        return x[pos:end]

    @staticmethod
    def sort(x,f):
        x.sort(key= python_lib_Functools.cmp_to_key(f))

    @staticmethod
    def splice(x,pos,_hx_len):
        if (pos < 0):
            pos = (len(x) + pos)
        if (pos < 0):
            pos = 0
        res = x[pos:(pos + _hx_len)]
        del x[pos:(pos + _hx_len)]
        return res

    @staticmethod
    def map(x,f):
        return list(map(f,x))

    @staticmethod
    def filter(x,f):
        return list(filter(f,x))

    @staticmethod
    def insert(a,pos,x):
        a.insert(pos, x)

    @staticmethod
    def reverse(a):
        a.reverse()

    @staticmethod
    def _get(x,idx):
        if ((idx > -1) and ((idx < len(x)))):
            return x[idx]
        else:
            return None

    @staticmethod
    def _set(x,idx,v):
        l = len(x)
        while (l < idx):
            x.append(None)
            l = (l + 1)
        if (l == idx):
            x.append(v)
        else:
            x[idx] = v
        return v

    @staticmethod
    def unsafeGet(x,idx):
        return x[idx]

    @staticmethod
    def unsafeSet(x,idx,val):
        x[idx] = val
        return val

    @staticmethod
    def resize(x,_hx_len):
        l = len(x)
        if (l < _hx_len):
            idx = (_hx_len - 1)
            v = None
            l1 = len(x)
            while (l1 < idx):
                x.append(None)
                l1 = (l1 + 1)
            if (l1 == idx):
                x.append(v)
            else:
                x[idx] = v
        elif (l > _hx_len):
            pos = _hx_len
            len1 = (l - _hx_len)
            if (pos < 0):
                pos = (len(x) + pos)
            if (pos < 0):
                pos = 0
            res = x[pos:(pos + len1)]
            del x[pos:(pos + len1)]
python_internal_ArrayImpl._hx_class = python_internal_ArrayImpl
_hx_classes["python.internal.ArrayImpl"] = python_internal_ArrayImpl


class HxOverrides:
    _hx_class_name = "HxOverrides"
    __slots__ = ()
    _hx_statics = ["iterator", "keyValueIterator", "eq", "stringOrNull", "shift", "pop", "push", "join", "filter", "map", "toUpperCase", "toLowerCase", "split", "length", "rshift", "modf", "mod", "arrayGet", "arraySet", "mapKwArgs", "reverseMapKwArgs"]

    @staticmethod
    def iterator(x):
        if isinstance(x,list):
            return haxe_iterators_ArrayIterator(x)
        return x.iterator()

    @staticmethod
    def keyValueIterator(x):
        if isinstance(x,list):
            return haxe_iterators_ArrayKeyValueIterator(x)
        return x.keyValueIterator()

    @staticmethod
    def eq(a,b):
        if (isinstance(a,list) or isinstance(b,list)):
            return a is b
        return (a == b)

    @staticmethod
    def stringOrNull(s):
        if (s is None):
            return "null"
        else:
            return s

    @staticmethod
    def shift(x):
        if isinstance(x,list):
            _this = x
            return (None if ((len(_this) == 0)) else _this.pop(0))
        return x.shift()

    @staticmethod
    def pop(x):
        if isinstance(x,list):
            _this = x
            return (None if ((len(_this) == 0)) else _this.pop())
        return x.pop()

    @staticmethod
    def push(x,e):
        if isinstance(x,list):
            _this = x
            _this.append(e)
            return len(_this)
        return x.push(e)

    @staticmethod
    def join(x,sep):
        if isinstance(x,list):
            return sep.join([python_Boot.toString1(x1,'') for x1 in x])
        return x.join(sep)

    @staticmethod
    def filter(x,f):
        if isinstance(x,list):
            return list(filter(f,x))
        return x.filter(f)

    @staticmethod
    def map(x,f):
        if isinstance(x,list):
            return list(map(f,x))
        return x.map(f)

    @staticmethod
    def toUpperCase(x):
        if isinstance(x,str):
            return x.upper()
        return x.toUpperCase()

    @staticmethod
    def toLowerCase(x):
        if isinstance(x,str):
            return x.lower()
        return x.toLowerCase()

    @staticmethod
    def split(x,delimiter):
        if isinstance(x,str):
            _this = x
            if (delimiter == ""):
                return list(_this)
            else:
                return _this.split(delimiter)
        return x.split(delimiter)

    @staticmethod
    def length(x):
        if isinstance(x,str):
            return len(x)
        elif isinstance(x,list):
            return len(x)
        return x.length

    @staticmethod
    def rshift(val,n):
        return ((val % 0x100000000) >> n)

    @staticmethod
    def modf(a,b):
        if (b == 0.0):
            return float('nan')
        elif (a < 0):
            if (b < 0):
                return -(-a % (-b))
            else:
                return -(-a % b)
        elif (b < 0):
            return a % (-b)
        else:
            return a % b

    @staticmethod
    def mod(a,b):
        if (a < 0):
            if (b < 0):
                return -(-a % (-b))
            else:
                return -(-a % b)
        elif (b < 0):
            return a % (-b)
        else:
            return a % b

    @staticmethod
    def arrayGet(a,i):
        if isinstance(a,list):
            x = a
            if ((i > -1) and ((i < len(x)))):
                return x[i]
            else:
                return None
        else:
            return a[i]

    @staticmethod
    def arraySet(a,i,v):
        if isinstance(a,list):
            x = a
            v1 = v
            l = len(x)
            while (l < i):
                x.append(None)
                l = (l + 1)
            if (l == i):
                x.append(v1)
            else:
                x[i] = v1
            return v1
        else:
            a[i] = v
            return v

    @staticmethod
    def mapKwArgs(a,v):
        a1 = _hx_AnonObject(python_Lib.anonToDict(a))
        k = python_HaxeIterator(iter(v.keys()))
        while k.hasNext():
            k1 = k.next()
            val = v.get(k1)
            if a1._hx_hasattr(k1):
                x = getattr(a1,k1)
                setattr(a1,val,x)
                delattr(a1,k1)
        return a1

    @staticmethod
    def reverseMapKwArgs(a,v):
        a1 = a.copy()
        k = python_HaxeIterator(iter(v.keys()))
        while k.hasNext():
            k1 = k.next()
            val = v.get(k1)
            if (val in a1):
                x = a1.get(val,None)
                a1[k1] = x
                del a1[val]
        return a1
HxOverrides._hx_class = HxOverrides
_hx_classes["HxOverrides"] = HxOverrides


class python_internal_Internal:
    _hx_class_name = "python.internal.Internal"
    __slots__ = ()
python_internal_Internal._hx_class = python_internal_Internal
_hx_classes["python.internal.Internal"] = python_internal_Internal


class python_internal_MethodClosure:
    _hx_class_name = "python.internal.MethodClosure"
    __slots__ = ("obj", "func")
    _hx_fields = ["obj", "func"]
    _hx_methods = ["__call__"]

    def __init__(self,obj,func):
        self.obj = obj
        self.func = func

    def __call__(self,*args):
        return self.func(self.obj,*args)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.obj = None
        _hx_o.func = None
python_internal_MethodClosure._hx_class = python_internal_MethodClosure
_hx_classes["python.internal.MethodClosure"] = python_internal_MethodClosure


class HxString:
    _hx_class_name = "HxString"
    __slots__ = ()
    _hx_statics = ["split", "charCodeAt", "charAt", "lastIndexOf", "toUpperCase", "toLowerCase", "indexOf", "indexOfImpl", "toString", "get_length", "fromCharCode", "substring", "substr"]

    @staticmethod
    def split(s,d):
        if (d == ""):
            return list(s)
        else:
            return s.split(d)

    @staticmethod
    def charCodeAt(s,index):
        if ((((s is None) or ((len(s) == 0))) or ((index < 0))) or ((index >= len(s)))):
            return None
        else:
            return ord(s[index])

    @staticmethod
    def charAt(s,index):
        if ((index < 0) or ((index >= len(s)))):
            return ""
        else:
            return s[index]

    @staticmethod
    def lastIndexOf(s,_hx_str,startIndex = None):
        if (startIndex is None):
            return s.rfind(_hx_str, 0, len(s))
        elif (_hx_str == ""):
            length = len(s)
            if (startIndex < 0):
                startIndex = (length + startIndex)
                if (startIndex < 0):
                    startIndex = 0
            if (startIndex > length):
                return length
            else:
                return startIndex
        else:
            i = s.rfind(_hx_str, 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len(_hx_str))) if ((i == -1)) else (i + 1))
            check = s.find(_hx_str, startLeft, len(s))
            if ((check > i) and ((check <= startIndex))):
                return check
            else:
                return i

    @staticmethod
    def toUpperCase(s):
        return s.upper()

    @staticmethod
    def toLowerCase(s):
        return s.lower()

    @staticmethod
    def indexOf(s,_hx_str,startIndex = None):
        if (startIndex is None):
            return s.find(_hx_str)
        else:
            return HxString.indexOfImpl(s,_hx_str,startIndex)

    @staticmethod
    def indexOfImpl(s,_hx_str,startIndex):
        if (_hx_str == ""):
            length = len(s)
            if (startIndex < 0):
                startIndex = (length + startIndex)
                if (startIndex < 0):
                    startIndex = 0
            if (startIndex > length):
                return length
            else:
                return startIndex
        return s.find(_hx_str, startIndex)

    @staticmethod
    def toString(s):
        return s

    @staticmethod
    def get_length(s):
        return len(s)

    @staticmethod
    def fromCharCode(code):
        return "".join(map(chr,[code]))

    @staticmethod
    def substring(s,startIndex,endIndex = None):
        if (startIndex < 0):
            startIndex = 0
        if (endIndex is None):
            return s[startIndex:]
        else:
            if (endIndex < 0):
                endIndex = 0
            if (endIndex < startIndex):
                return s[endIndex:startIndex]
            else:
                return s[startIndex:endIndex]

    @staticmethod
    def substr(s,startIndex,_hx_len = None):
        if (_hx_len is None):
            return s[startIndex:]
        else:
            if (_hx_len == 0):
                return ""
            if (startIndex < 0):
                startIndex = (len(s) + startIndex)
                if (startIndex < 0):
                    startIndex = 0
            return s[startIndex:(startIndex + _hx_len)]
HxString._hx_class = HxString
_hx_classes["HxString"] = HxString


class python_io_NativeInput(haxe_io_Input):
    _hx_class_name = "python.io.NativeInput"
    __slots__ = ("stream", "wasEof")
    _hx_fields = ["stream", "wasEof"]
    _hx_methods = ["get_canSeek", "close", "tell", "throwEof", "eof", "readinto", "seek", "readBytes"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Input


    def __init__(self,s):
        self.wasEof = None
        self.stream = s
        self.set_bigEndian(False)
        self.wasEof = False
        if (not self.stream.readable()):
            raise haxe_Exception.thrown("Write-only stream")

    def get_canSeek(self):
        return self.stream.seekable()

    def close(self):
        self.stream.close()

    def tell(self):
        return self.stream.tell()

    def throwEof(self):
        self.wasEof = True
        raise haxe_Exception.thrown(haxe_io_Eof())

    def eof(self):
        return self.wasEof

    def readinto(self,b):
        raise haxe_Exception.thrown("abstract method, should be overridden")

    def seek(self,p,mode):
        raise haxe_Exception.thrown("abstract method, should be overridden")

    def readBytes(self,s,pos,_hx_len):
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > s.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        ba = bytearray(_hx_len)
        ret = self.readinto(ba)
        if (ret == 0):
            self.throwEof()
        s.blit(pos,haxe_io_Bytes.ofData(ba),0,_hx_len)
        return ret

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.stream = None
        _hx_o.wasEof = None
python_io_NativeInput._hx_class = python_io_NativeInput
_hx_classes["python.io.NativeInput"] = python_io_NativeInput


class python_io_IInput:
    _hx_class_name = "python.io.IInput"
    __slots__ = ("bigEndian",)
    _hx_fields = ["bigEndian"]
    _hx_methods = ["set_bigEndian", "readByte", "readBytes", "close", "readAll", "readFullBytes", "read", "readUntil", "readLine", "readFloat", "readDouble", "readInt8", "readInt16", "readUInt16", "readInt24", "readUInt24", "readInt32", "readString"]
python_io_IInput._hx_class = python_io_IInput
_hx_classes["python.io.IInput"] = python_io_IInput


class python_io_NativeBytesInput(python_io_NativeInput):
    _hx_class_name = "python.io.NativeBytesInput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["readByte", "seek", "readinto"]
    _hx_statics = []
    _hx_interfaces = [python_io_IInput]
    _hx_super = python_io_NativeInput


    def __init__(self,stream):
        super().__init__(stream)

    def readByte(self):
        ret = self.stream.read(1)
        if (len(ret) == 0):
            self.throwEof()
        return ret[0]

    def seek(self,p,pos):
        self.wasEof = False
        python_io_IoTools.seekInBinaryMode(self.stream,p,pos)

    def readinto(self,b):
        return self.stream.readinto(b)

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
python_io_NativeBytesInput._hx_class = python_io_NativeBytesInput
_hx_classes["python.io.NativeBytesInput"] = python_io_NativeBytesInput


class python_io_IFileInput:
    _hx_class_name = "python.io.IFileInput"
    __slots__ = ()
    _hx_methods = ["seek", "tell", "eof"]
    _hx_interfaces = [python_io_IInput]
python_io_IFileInput._hx_class = python_io_IFileInput
_hx_classes["python.io.IFileInput"] = python_io_IFileInput


class python_io_FileBytesInput(python_io_NativeBytesInput):
    _hx_class_name = "python.io.FileBytesInput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = [python_io_IFileInput]
    _hx_super = python_io_NativeBytesInput


    def __init__(self,stream):
        super().__init__(stream)
python_io_FileBytesInput._hx_class = python_io_FileBytesInput
_hx_classes["python.io.FileBytesInput"] = python_io_FileBytesInput


class python_io_NativeOutput(haxe_io_Output):
    _hx_class_name = "python.io.NativeOutput"
    __slots__ = ("stream",)
    _hx_fields = ["stream"]
    _hx_methods = ["get_canSeek", "close", "prepare", "flush", "tell"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Output


    def __init__(self,stream):
        self.stream = None
        self.set_bigEndian(False)
        self.stream = stream
        if (not stream.writable()):
            raise haxe_Exception.thrown("Read only stream")

    def get_canSeek(self):
        return self.stream.seekable()

    def close(self):
        self.stream.close()

    def prepare(self,nbytes):
        self.stream.truncate(nbytes)

    def flush(self):
        self.stream.flush()

    def tell(self):
        return self.stream.tell()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.stream = None
python_io_NativeOutput._hx_class = python_io_NativeOutput
_hx_classes["python.io.NativeOutput"] = python_io_NativeOutput


class python_io_NativeBytesOutput(python_io_NativeOutput):
    _hx_class_name = "python.io.NativeBytesOutput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["seek", "prepare", "writeByte", "writeBytes"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = python_io_NativeOutput


    def __init__(self,stream):
        super().__init__(stream)

    def seek(self,p,pos):
        python_io_IoTools.seekInBinaryMode(self.stream,p,pos)

    def prepare(self,nbytes):
        self.stream.truncate(nbytes)

    def writeByte(self,c):
        self.stream.write(bytearray([c]))

    def writeBytes(self,s,pos,_hx_len):
        return self.stream.write(s.b[pos:(pos + _hx_len)])

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
python_io_NativeBytesOutput._hx_class = python_io_NativeBytesOutput
_hx_classes["python.io.NativeBytesOutput"] = python_io_NativeBytesOutput


class python_io_IOutput:
    _hx_class_name = "python.io.IOutput"
    __slots__ = ("bigEndian",)
    _hx_fields = ["bigEndian"]
    _hx_methods = ["set_bigEndian", "writeByte", "writeBytes", "flush", "close", "write", "writeFullBytes", "writeFloat", "writeDouble", "writeInt8", "writeInt16", "writeUInt16", "writeInt24", "writeUInt24", "writeInt32", "prepare", "writeInput", "writeString"]
python_io_IOutput._hx_class = python_io_IOutput
_hx_classes["python.io.IOutput"] = python_io_IOutput


class python_io_IFileOutput:
    _hx_class_name = "python.io.IFileOutput"
    __slots__ = ()
    _hx_methods = ["seek", "tell"]
    _hx_interfaces = [python_io_IOutput]
python_io_IFileOutput._hx_class = python_io_IFileOutput
_hx_classes["python.io.IFileOutput"] = python_io_IFileOutput


class python_io_FileBytesOutput(python_io_NativeBytesOutput):
    _hx_class_name = "python.io.FileBytesOutput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = [python_io_IFileOutput]
    _hx_super = python_io_NativeBytesOutput


    def __init__(self,stream):
        super().__init__(stream)
python_io_FileBytesOutput._hx_class = python_io_FileBytesOutput
_hx_classes["python.io.FileBytesOutput"] = python_io_FileBytesOutput


class python_io_NativeTextInput(python_io_NativeInput):
    _hx_class_name = "python.io.NativeTextInput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["readByte", "seek", "readinto"]
    _hx_statics = []
    _hx_interfaces = [python_io_IInput]
    _hx_super = python_io_NativeInput


    def __init__(self,stream):
        super().__init__(stream)

    def readByte(self):
        ret = self.stream.buffer.read(1)
        if (len(ret) == 0):
            self.throwEof()
        return ret[0]

    def seek(self,p,pos):
        self.wasEof = False
        python_io_IoTools.seekInTextMode(self.stream,self.tell,p,pos)

    def readinto(self,b):
        return self.stream.buffer.readinto(b)

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
python_io_NativeTextInput._hx_class = python_io_NativeTextInput
_hx_classes["python.io.NativeTextInput"] = python_io_NativeTextInput


class python_io_FileTextInput(python_io_NativeTextInput):
    _hx_class_name = "python.io.FileTextInput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = [python_io_IFileInput]
    _hx_super = python_io_NativeTextInput


    def __init__(self,stream):
        super().__init__(stream)
python_io_FileTextInput._hx_class = python_io_FileTextInput
_hx_classes["python.io.FileTextInput"] = python_io_FileTextInput


class python_io_NativeTextOutput(python_io_NativeOutput):
    _hx_class_name = "python.io.NativeTextOutput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["seek", "writeBytes", "writeByte"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = python_io_NativeOutput


    def __init__(self,stream):
        super().__init__(stream)
        if (not stream.writable()):
            raise haxe_Exception.thrown("Read only stream")

    def seek(self,p,pos):
        python_io_IoTools.seekInTextMode(self.stream,self.tell,p,pos)

    def writeBytes(self,s,pos,_hx_len):
        return self.stream.buffer.write(s.b[pos:(pos + _hx_len)])

    def writeByte(self,c):
        self.stream.write("".join(map(chr,[c])))

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
python_io_NativeTextOutput._hx_class = python_io_NativeTextOutput
_hx_classes["python.io.NativeTextOutput"] = python_io_NativeTextOutput


class python_io_FileTextOutput(python_io_NativeTextOutput):
    _hx_class_name = "python.io.FileTextOutput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = [python_io_IFileOutput]
    _hx_super = python_io_NativeTextOutput


    def __init__(self,stream):
        super().__init__(stream)
python_io_FileTextOutput._hx_class = python_io_FileTextOutput
_hx_classes["python.io.FileTextOutput"] = python_io_FileTextOutput


class python_io_IoTools:
    _hx_class_name = "python.io.IoTools"
    __slots__ = ()
    _hx_statics = ["createFileInputFromText", "createFileInputFromBytes", "createFileOutputFromText", "createFileOutputFromBytes", "seekInTextMode", "seekInBinaryMode"]

    @staticmethod
    def createFileInputFromText(t):
        return sys_io_FileInput(python_io_FileTextInput(t))

    @staticmethod
    def createFileInputFromBytes(t):
        return sys_io_FileInput(python_io_FileBytesInput(t))

    @staticmethod
    def createFileOutputFromText(t):
        return sys_io_FileOutput(python_io_FileTextOutput(t))

    @staticmethod
    def createFileOutputFromBytes(t):
        return sys_io_FileOutput(python_io_FileBytesOutput(t))

    @staticmethod
    def seekInTextMode(stream,tell,p,pos):
        pos1 = None
        pos2 = pos.index
        if (pos2 == 0):
            pos1 = 0
        elif (pos2 == 1):
            p = (tell() + p)
            pos1 = 0
        elif (pos2 == 2):
            stream.seek(0,2)
            p = (tell() + p)
            pos1 = 0
        else:
            pass
        stream.seek(p,pos1)

    @staticmethod
    def seekInBinaryMode(stream,p,pos):
        pos1 = None
        pos2 = pos.index
        if (pos2 == 0):
            pos1 = 0
        elif (pos2 == 1):
            pos1 = 1
        elif (pos2 == 2):
            pos1 = 2
        else:
            pass
        stream.seek(p,pos1)
python_io_IoTools._hx_class = python_io_IoTools
_hx_classes["python.io.IoTools"] = python_io_IoTools


class python_lib__Re_Choice_Impl_:
    _hx_class_name = "python.lib._Re.Choice_Impl_"
    __slots__ = ()
    _hx_statics = ["fromA", "fromB"]

    @staticmethod
    def fromA(x):
        return x

    @staticmethod
    def fromB(x):
        return x
python_lib__Re_Choice_Impl_._hx_class = python_lib__Re_Choice_Impl_
_hx_classes["python.lib._Re.Choice_Impl_"] = python_lib__Re_Choice_Impl_


class python_lib__Re_RegexHelper:
    _hx_class_name = "python.lib._Re.RegexHelper"
    __slots__ = ()
    _hx_statics = ["findallDynamic"]

    @staticmethod
    def findallDynamic(r,string,pos = None,endpos = None):
        if (endpos is None):
            if (pos is None):
                return r.findall(string)
            else:
                return r.findall(string,pos)
        else:
            return r.findall(string,pos,endpos)
python_lib__Re_RegexHelper._hx_class = python_lib__Re_RegexHelper
_hx_classes["python.lib._Re.RegexHelper"] = python_lib__Re_RegexHelper


class sys_io_File:
    _hx_class_name = "sys.io.File"
    __slots__ = ()
    _hx_statics = ["getContent", "saveContent", "getBytes", "saveBytes", "read", "write", "append", "update", "copy"]

    @staticmethod
    def getContent(path):
        f = python_lib_Builtins.open(path,"r",-1,"utf-8",None,"")
        content = f.read(-1)
        f.close()
        return content

    @staticmethod
    def saveContent(path,content):
        f = python_lib_Builtins.open(path,"w",-1,"utf-8",None,"")
        f.write(content)
        f.close()

    @staticmethod
    def getBytes(path):
        f = python_lib_Builtins.open(path,"rb",-1)
        size = f.read(-1)
        b = haxe_io_Bytes.ofData(size)
        f.close()
        return b

    @staticmethod
    def saveBytes(path,_hx_bytes):
        f = python_lib_Builtins.open(path,"wb",-1)
        f.write(_hx_bytes.b)
        f.close()

    @staticmethod
    def read(path,binary = None):
        if (binary is None):
            binary = True
        mode = ("rb" if binary else "r")
        f = python_lib_Builtins.open(path,mode,-1,None,None,(None if binary else ""))
        if binary:
            return python_io_IoTools.createFileInputFromBytes(f)
        else:
            return python_io_IoTools.createFileInputFromText(f)

    @staticmethod
    def write(path,binary = None):
        if (binary is None):
            binary = True
        mode = ("wb" if binary else "w")
        f = python_lib_Builtins.open(path,mode,-1,None,None,(None if binary else ""))
        if binary:
            return python_io_IoTools.createFileOutputFromBytes(f)
        else:
            return python_io_IoTools.createFileOutputFromText(f)

    @staticmethod
    def append(path,binary = None):
        if (binary is None):
            binary = True
        mode = ("ab" if binary else "a")
        f = python_lib_Builtins.open(path,mode,-1,None,None,(None if binary else ""))
        if binary:
            return python_io_IoTools.createFileOutputFromBytes(f)
        else:
            return python_io_IoTools.createFileOutputFromText(f)

    @staticmethod
    def update(path,binary = None):
        if (binary is None):
            binary = True
        if (not sys_FileSystem.exists(path)):
            sys_io_File.write(path).close()
        mode = ("rb+" if binary else "r+")
        f = python_lib_Builtins.open(path,mode,-1,None,None,(None if binary else ""))
        if binary:
            return python_io_IoTools.createFileOutputFromBytes(f)
        else:
            return python_io_IoTools.createFileOutputFromText(f)

    @staticmethod
    def copy(srcPath,dstPath):
        python_lib_Shutil.copy(srcPath,dstPath)
sys_io_File._hx_class = sys_io_File
_hx_classes["sys.io.File"] = sys_io_File


class sys_io_FileInput(haxe_io_Input):
    _hx_class_name = "sys.io.FileInput"
    __slots__ = ("impl",)
    _hx_fields = ["impl"]
    _hx_methods = ["set_bigEndian", "seek", "tell", "eof", "readByte", "readBytes", "close", "readAll", "readFullBytes", "read", "readUntil", "readLine", "readFloat", "readDouble", "readInt8", "readInt16", "readUInt16", "readInt24", "readUInt24", "readInt32", "readString"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Input


    def __init__(self,impl):
        self.impl = impl

    def set_bigEndian(self,b):
        return self.impl.set_bigEndian(b)

    def seek(self,p,pos):
        self.impl.seek(p,pos)

    def tell(self):
        return self.impl.tell()

    def eof(self):
        return self.impl.eof()

    def readByte(self):
        return self.impl.readByte()

    def readBytes(self,s,pos,_hx_len):
        return self.impl.readBytes(s,pos,_hx_len)

    def close(self):
        self.impl.close()

    def readAll(self,bufsize = None):
        return self.impl.readAll(bufsize)

    def readFullBytes(self,s,pos,_hx_len):
        self.impl.readFullBytes(s,pos,_hx_len)

    def read(self,nbytes):
        return self.impl.read(nbytes)

    def readUntil(self,end):
        return self.impl.readUntil(end)

    def readLine(self):
        return self.impl.readLine()

    def readFloat(self):
        return self.impl.readFloat()

    def readDouble(self):
        return self.impl.readDouble()

    def readInt8(self):
        return self.impl.readInt8()

    def readInt16(self):
        return self.impl.readInt16()

    def readUInt16(self):
        return self.impl.readUInt16()

    def readInt24(self):
        return self.impl.readInt24()

    def readUInt24(self):
        return self.impl.readUInt24()

    def readInt32(self):
        return self.impl.readInt32()

    def readString(self,_hx_len,encoding = None):
        return self.impl.readString(_hx_len)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.impl = None
sys_io_FileInput._hx_class = sys_io_FileInput
_hx_classes["sys.io.FileInput"] = sys_io_FileInput


class sys_io_FileOutput(haxe_io_Output):
    _hx_class_name = "sys.io.FileOutput"
    __slots__ = ("impl",)
    _hx_fields = ["impl"]
    _hx_methods = ["seek", "tell", "set_bigEndian", "writeByte", "writeBytes", "flush", "close", "write", "writeFullBytes", "writeFloat", "writeDouble", "writeInt8", "writeInt16", "writeUInt16", "writeInt24", "writeUInt24", "writeInt32", "prepare", "writeInput", "writeString"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Output


    def __init__(self,impl):
        self.impl = impl

    def seek(self,p,pos):
        self.impl.seek(p,pos)

    def tell(self):
        return self.impl.tell()

    def set_bigEndian(self,b):
        return self.impl.set_bigEndian(b)

    def writeByte(self,c):
        self.impl.writeByte(c)

    def writeBytes(self,s,pos,_hx_len):
        return self.impl.writeBytes(s,pos,_hx_len)

    def flush(self):
        self.impl.flush()

    def close(self):
        self.impl.close()

    def write(self,s):
        self.impl.write(s)

    def writeFullBytes(self,s,pos,_hx_len):
        self.impl.writeFullBytes(s,pos,_hx_len)

    def writeFloat(self,x):
        self.impl.writeFloat(x)

    def writeDouble(self,x):
        self.impl.writeDouble(x)

    def writeInt8(self,x):
        self.impl.writeInt8(x)

    def writeInt16(self,x):
        self.impl.writeInt16(x)

    def writeUInt16(self,x):
        self.impl.writeUInt16(x)

    def writeInt24(self,x):
        self.impl.writeInt24(x)

    def writeUInt24(self,x):
        self.impl.writeUInt24(x)

    def writeInt32(self,x):
        self.impl.writeInt32(x)

    def prepare(self,nbytes):
        self.impl.prepare(nbytes)

    def writeInput(self,i,bufsize = None):
        self.impl.writeInput(i,bufsize)

    def writeString(self,s,encoding = None):
        self.impl.writeString(s)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.impl = None
sys_io_FileOutput._hx_class = sys_io_FileOutput
_hx_classes["sys.io.FileOutput"] = sys_io_FileOutput

class sys_io_FileSeek(Enum):
    __slots__ = ()
    _hx_class_name = "sys.io.FileSeek"
    _hx_constructs = ["SeekBegin", "SeekCur", "SeekEnd"]
sys_io_FileSeek.SeekBegin = sys_io_FileSeek("SeekBegin", 0, ())
sys_io_FileSeek.SeekCur = sys_io_FileSeek("SeekCur", 1, ())
sys_io_FileSeek.SeekEnd = sys_io_FileSeek("SeekEnd", 2, ())
sys_io_FileSeek._hx_class = sys_io_FileSeek
_hx_classes["sys.io.FileSeek"] = sys_io_FileSeek

Math.NEGATIVE_INFINITY = float("-inf")
Math.POSITIVE_INFINITY = float("inf")
Math.NaN = float("nan")
Math.PI = python_lib_Math.pi

CompileTimeClassList.__meta__ = _hx_AnonObject({'obj': _hx_AnonObject({'classLists': [["null,true,pyextern.Processor", "pyextern.Process_numpy,pyextern.Process_pandas,pyextern.Process_pyqt5"]]})})
CompileTimeClassList.lists = None
haxe_SysTools.winMetaCharacters = [32, 40, 41, 37, 33, 94, 34, 60, 62, 38, 124, 10, 13, 44, 59]
StringTools.winMetaCharacters = haxe_SysTools.winMetaCharacters
Sys._programPath = sys_FileSystem.fullPath(python_lib_Inspect.getsourcefile(Sys))
_Xml_XmlType_Impl_.Element = 0
_Xml_XmlType_Impl_.PCData = 1
_Xml_XmlType_Impl_.CData = 2
_Xml_XmlType_Impl_.Comment = 3
_Xml_XmlType_Impl_.DocType = 4
_Xml_XmlType_Impl_.ProcessingInstruction = 5
_Xml_XmlType_Impl_.Document = 6
Xml.Element = 0
Xml.PCData = 1
Xml.CData = 2
Xml.Comment = 3
Xml.DocType = 4
Xml.ProcessingInstruction = 5
Xml.Document = 6
def _hx_init_haxe_io_FPHelper_i64tmp():
    def _hx_local_0():
        this1 = haxe__Int64____Int64(0,0)
        return this1
    return _hx_local_0()
haxe_io_FPHelper.i64tmp = _hx_init_haxe_io_FPHelper_i64tmp()
haxe_io_FPHelper.LN2 = 0.6931471805599453
def _hx_init_haxe_xml_Parser_escapes():
    def _hx_local_0():
        h = haxe_ds_StringMap()
        h.h["lt"] = "<"
        h.h["gt"] = ">"
        h.h["amp"] = "&"
        h.h["quot"] = "\""
        h.h["apos"] = "'"
        return h
    return _hx_local_0()
haxe_xml_Parser.escapes = _hx_init_haxe_xml_Parser_escapes()
pyextern_Main.re_ident = EReg("^[A-Za-z_][A-Za-z0-9_]*$","")
pyextern_Main.re_type = EReg("^[A-Z_][A-Za-z0-9_]*$","")
pyextern_Processor.rstParser = docutils_parsers_rst_Parser()
pyextern_Process_numpy.__meta__ = _hx_AnonObject({'obj': _hx_AnonObject({'process_modules': ["numpy"]})})
pyextern_Process_pandas.__meta__ = _hx_AnonObject({'obj': _hx_AnonObject({'process_modules': ["pandas"]})})
pyextern_Process_pyqt5.__meta__ = _hx_AnonObject({'obj': _hx_AnonObject({'process_modules': ["PyQt5", "PySide2"]})})
python_Boot.keywords = set(["and", "del", "from", "not", "with", "as", "elif", "global", "or", "yield", "assert", "else", "if", "pass", "None", "break", "except", "import", "raise", "True", "class", "exec", "in", "return", "False", "continue", "finally", "is", "try", "def", "for", "lambda", "while"])
python_Boot.prefixLength = len("_hx_")
python_Lib.lineEnd = ("\r\n" if ((Sys.systemName() == "Windows")) else "\n")

pyextern_Main.main()
