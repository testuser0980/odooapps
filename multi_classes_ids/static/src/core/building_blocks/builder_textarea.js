import {Component} from "@odoo/owl";
import {pick} from "@web/core/utils/objects";
import {BuilderTextAreaBase, textAreaBasePassthroughProps} from "./builder_textarea_base";
import {
    basicContainerBuilderComponentProps,
    useInputBuilderComponent,
    useBuilderComponent,
} from "@html_builder/core/utils";
import {BuilderComponent} from "@html_builder/core/building_blocks/builder_component";

export class BuilderTextArea extends Component {
    static template = "multi_classes_ids.BuilderTextArea";
    static props = {
        ...basicContainerBuilderComponentProps,
        textAreaBasePassthroughProps,
        prefix: {type: String, optional: true},
        default: {type: String, optional: true},
    };
    static components = {
        BuilderComponent,
        BuilderTextAreaBase,
    };

    setup() {
        useBuilderComponent();
        const {state, commit, preview} = useInputBuilderComponent({
            id: this.props.id,
            defaultValue: this.props.default,
        });
        this.commit = commit;
        this.preview = preview;
        this.state = state;
    }

    // get textInputBaseProps() {
    // return pick(this.props, ...Object.keys(textInputBasePassthroughProps));
    // }
}
