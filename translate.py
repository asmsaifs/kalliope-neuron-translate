import logging

from kalliope.core.NeuronModule import NeuronModule, InvalidParameterException
from googletrans import Translator

logging.basicConfig()
logger = logging.getLogger("kalliope")


class Translate(NeuronModule):
    def __init__(self, **kwargs):
        # we don't need the TTS cache for this neuron
        cache = kwargs.get('cache', None)
        if cache is None:
            cache = False
            kwargs["cache"] = cache
        super(Translate, self).__init__(**kwargs)

        self.message = None

        # get parameters form the neuron
        self.lang_out = kwargs.get('lang_out', None)
        self.lang_in = kwargs.get('lang_in', 'auto')
        self.sentence = kwargs.get('sentence', None)

        # check parameters
        if self._is_parameters_ok():
            result = Translator().translate(
                self.sentence, dest=self.lang_out, src=self.lang_in).text
            lang_detect = Translator().detect(self.sentence).lang

            self.message = {
                "result": result,
                "lang_in": lang_detect,
                "lang_out": self.lang_out
            }

            logger.debug("Translate returned message: %s" % str(self.message))
            self.say(self.message)
    
    def _is_parameters_ok(self):
        """
        Check if received parameters are ok to perform operations in the neuron
        :return: true if parameters are ok, raise an exception otherwise
        .. raises:: InvalidParameterException
        """

        if self.lang_out is None:
            raise InvalidParameterException("Needs Lang out")

        if self.lang_in is None:
            raise InvalidParameterException("Needs Lang in")

        if self.sentence is None:
            raise InvalidParameterException("Needs sentence")

        return True
