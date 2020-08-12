# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Dialog(Component):
    """A Dialog component.
Material UI Dialog component

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): Children to render inside of the Dialog
- id (string; required): Dialog ID
- ariaLabelledBy (string; default ''): List of space separated id's of elements to use as aria labels
- actions (optional): Actions component or list of components for the Dialog
- className (string; default ''): CSS class name of the root element
- open (boolean; default False): Is the dialog open?

IMPORTANT: When using this component in Dash, a listener must be set up (either as state or
an input) for this component's props.open value in order to achieve the desired behavior.
If such a listener is not in place, the non-modal version of this dialog will contaminate
other callbacks in the browser
- autoScrollBodyContent (boolean; default False): If set to true, the body content of the Dialog will be scrollable.
- actionsContainerClassName (string; optional): The className to add to the actions container's root element.
- bodyClassName (string; optional): The className to add to the content's root element under the title.
- componentContainerClassName (string; optional): The className to add to the component container
- contentClassName (string; optional): The className to add to the content container
- fullWidth (boolean; default True): Determines whether the Dialog is the full width of the container
- overlayClassName (string; optional): The className to add to the Overlay component rendered behind the Dialog
- paperClassName (string; optional): CSS class name of the Paper element
- titleClassName (string; optional): The className to add to the title's root container element
- useBrowserSideClose (boolean; default False): If set to true, the Close Icon will show in the upper right corner of the dialog, closing the Dialog browser side
- scroll (dict; optional): "paper" or "body", Determines scroll container
- style (dict; optional): Styles to be implemented as inline css"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.REQUIRED, ariaLabelledBy=Component.UNDEFINED, actions=Component.UNDEFINED, className=Component.UNDEFINED, open=Component.UNDEFINED, autoScrollBodyContent=Component.UNDEFINED, actionsContainerClassName=Component.UNDEFINED, bodyClassName=Component.UNDEFINED, componentContainerClassName=Component.UNDEFINED, contentClassName=Component.UNDEFINED, fullWidth=Component.UNDEFINED, overlayClassName=Component.UNDEFINED, paperClassName=Component.UNDEFINED, titleClassName=Component.UNDEFINED, useBrowserSideClose=Component.UNDEFINED, scroll=Component.UNDEFINED, style=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'ariaLabelledBy', 'actions', 'className', 'open', 'autoScrollBodyContent', 'actionsContainerClassName', 'bodyClassName', 'componentContainerClassName', 'contentClassName', 'fullWidth', 'overlayClassName', 'paperClassName', 'titleClassName', 'useBrowserSideClose', 'scroll', 'style']
        self._type = 'Dialog'
        self._namespace = 'sd_material_ui'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'ariaLabelledBy', 'actions', 'className', 'open', 'autoScrollBodyContent', 'actionsContainerClassName', 'bodyClassName', 'componentContainerClassName', 'contentClassName', 'fullWidth', 'overlayClassName', 'paperClassName', 'titleClassName', 'useBrowserSideClose', 'scroll', 'style']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['id']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Dialog, self).__init__(children=children, **args)
