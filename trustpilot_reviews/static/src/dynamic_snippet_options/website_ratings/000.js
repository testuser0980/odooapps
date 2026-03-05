/** @odoo-module **/

import {groupBy} from "@web/core/utils/arrays";
import publicWidget from "@web/legacy/js/public/public_widget";
import DynamicSnippetCarousel from "@website/snippets/s_dynamic_snippet_carousel/000";
var registry = publicWidget.registry;

const DynamicSnippetRatings = DynamicSnippetCarousel.extend({
    // While the selector has 'upcoming_snippet' in its name, it now has a filter
    // option to include ongoing events. The name is kept for backward compatibility.
    selector: "._dynamic_snippet_ratings",
    disabledInEditableMode: false,

    init: function () {
        this._super.apply(this, arguments);
        this.template_key = "theme_axiom._dynamic_snippet";
    },
    /**
     * @override
     * @private
     */
    _getSearchDomain: function () {
        let searchDomain = this._super.apply(this, arguments);
        const filterByTagIds = this.$el.get(0).dataset.ratingsIds;
        if (filterByTagIds) {
            let tagGroupedByRating = groupBy(
                JSON.parse(filterByTagIds),
                "id"
            );
            for (const category in tagGroupedByRating) {
                searchDomain = searchDomain.concat([
                    ["id", "in", tagGroupedByRating[category].map((e) => e.id)],
                ]);
            }
        }
        const allIds = searchDomain
            .filter(([field, operator]) => field === "id" && operator === "in")
            .flatMap(([, , ids]) => ids);
        const mergedIds = [...new Set(allIds)];
        searchDomain =
            searchDomain.length > 0 ? [["id", "in", mergedIds]] : [];
        return searchDomain;
    },
});

publicWidget.registry.ratings = DynamicSnippetRatings;
