# library imports
import os
import numpy as np
import matplotlib.pyplot as plt

# project imports
from consts import *


class Plotter:
    """
    A class responsible to generate plots from data
    """

    # CONSTS #

    # END - CONSTS #

    def __init__(self):
        pass

    @staticmethod
    def hist(data: list,
             x_label: str,
             y_label: str,
             save_path: str,
             xlim: tuple = None,
             ylim: tuple = None,
             normalize: bool = False):
        plt.hist(x=data,
                 density=normalize,
                 color="blue")
        plt.xlabel(x_label, fontsize=14)
        plt.ylabel(y_label, fontsize=14)
        if isinstance(xlim, tuple) and len(xlim) == 2:
            plt.xlim(xlim[0], xlim[1])
        if isinstance(ylim, tuple) and len(ylim) == 2:
            plt.ylim(ylim[0], ylim[1])
        plt.tight_layout()
        plt.savefig(save_path, dpi=300)
        plt.close()

    @staticmethod
    def bar_std(x: list,
                y: list,
                y_err: list,
                x_label: str,
                y_label: str,
                save_path: str,
                x_names: list = None,
                ylim: tuple = None):
        plt.bar(x=x,
                height=y,
                width=0.8,
                color="blue")
        plt.errorbar(x=x,
                     y=y,
                     yerr=y_err,
                     fmt=".",
                     markersize=0,
                     capsize=4,
                     color="black")
        plt.xlabel(x_label, fontsize=14)
        plt.ylabel(y_label, fontsize=14)
        if isinstance(ylim, tuple) and len(ylim) == 2:
            plt.ylim(ylim[0], ylim[1])
        if isinstance(x_names, list) and len(x_names) == len(x):
            plt.xticks(x, x_names, fontsize=10)
        plt.tight_layout()
        plt.savefig(save_path, dpi=300)
        plt.close()

    @staticmethod
    def bar(x: list,
            y: list,
            x_label: str,
            y_label: str,
            save_path: str,
            x_names: list = None,
            ylim: tuple = None):
        plt.bar(x=x,
                height=y,
                width=0.8,
                color="blue")
        plt.xlabel(x_label, fontsize=14)
        plt.ylabel(y_label, fontsize=14)
        if isinstance(ylim, tuple) and len(ylim) == 2:
            plt.ylim(ylim[0], ylim[1])
        if isinstance(x_names, list) and len(x_names) == len(x):
            plt.xticks(x, x_names, fontsize=10)
        plt.tight_layout()
        plt.savefig(save_path, dpi=300)
        plt.close()
